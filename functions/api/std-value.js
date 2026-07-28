/**
 * GET /api/std-value?type=apt|house|land&year=2026&legalDongCd=...&bdMgtSn=...&jibun=...
 * 공시가격 조회 프록시 (공공데이터포털)
 *
 * ENV (Cloudflare Pages > Settings > Environment Variables, 모두 Encrypted):
 *   PUBLIC_DATA_KEY — data.go.kr 인증키 (3개 API 공통)
 *
 * type별 호출 API:
 *   apt   → 국토교통부_공동주택공시가격정보서비스
 *   house → 국토교통부_개별주택가격정보서비스
 *   land  → 국토교통부_개별공시지가정보서비스
 */
export async function onRequestGet(context) {
  const { request, env } = context;
  const url = new URL(request.url);
  const type = url.searchParams.get('type') || 'apt';
  const year = url.searchParams.get('year') || String(new Date().getFullYear());
  const legalDongCd = url.searchParams.get('legalDongCd') || '';
  const bdMgtSn = url.searchParams.get('bdMgtSn') || '';   // 건물관리번호 (apt용)
  const jibun = url.searchParams.get('jibun') || '';       // 번-지 (house/land용)

  /* ── MOCK (API 키 미등록 시) ── */
  if (!env.PUBLIC_DATA_KEY) {
    return json({
      _mock: true,
      type,
      year,
      stdValue: mockStdValue(type),
      unit: type === 'land' ? '원/㎡' : '원',
      label: type === 'land' ? '개별공시지가' : type === 'apt' ? '공동주택 공시가격' : '개별주택가격',
    });
  }

  /* ── 캐시 (Cloudflare Cache API, 24h — 공시가격은 연 1회 갱신이라 캐시 효율 최대) ── */
  const cacheKey = new Request(request.url);
  const cache = caches.default;
  const cached = await cache.match(cacheKey);
  if (cached) return cached;

  try {
    let result;
    if (type === 'apt') {
      result = await fetchAptPrice(env.PUBLIC_DATA_KEY, legalDongCd, bdMgtSn, year);
    } else if (type === 'house') {
      result = await fetchHousePrice(env.PUBLIC_DATA_KEY, legalDongCd, jibun, year);
    } else {
      result = await fetchLandPrice(env.PUBLIC_DATA_KEY, legalDongCd, jibun, year);
    }
    const response = json(result);
    const toCache = response.clone();
    toCache.headers.set('Cache-Control', 'public, max-age=86400');
    context.waitUntil(cache.put(cacheKey, toCache));
    return response;
  } catch (e) {
    return json({ error: e.message || '조회 중 오류가 발생했습니다.' }, 502);
  }
}

/* ── 공동주택 공시가격 ── */
async function fetchAptPrice(key, legalDongCd, bdMgtSn, year) {
  const lawd_cd = legalDongCd.slice(0, 5);   // 시군구코드 (앞 5자리)
  const endpoint = 'https://apis.data.go.kr/1611000/AptPriceInfo/getAptPriceInfo';
  const params = new URLSearchParams({
    serviceKey: key,
    LAWD_CD: lawd_cd,
    DEAL_YMD: `${year}01`,   // 공시기준 연월 (1월 기준)
    numOfRows: '1',
    pageNo: '1',
    type: 'json',
  });
  if (bdMgtSn) params.set('BLDG_MNG_NO', bdMgtSn);

  const resp = await fetch(`${endpoint}?${params}`);
  const data = await resp.json();
  const item = data?.response?.body?.items?.item?.[0];
  if (!item) throw new Error('공시가격 정보를 찾을 수 없습니다. 동·호수 또는 연도를 확인하세요.');
  return {
    type: 'apt',
    year,
    stdValue: Number(String(item.pblntfPc || '0').replace(/,/g, '')),
    unit: '원',
    label: '공동주택 공시가격',
    detail: `${item.aptNm || ''} ${item.floor || ''}층`,
  };
}

/* ── 개별주택가격 ── */
async function fetchHousePrice(key, legalDongCd, jibun, year) {
  const pnu = buildPnu(legalDongCd, jibun);
  const endpoint = 'https://apis.data.go.kr/1611000/IndvdHousingPriceInfo/getIndvdHousingPriceInfo';
  const params = new URLSearchParams({
    serviceKey: key,
    pnu,
    stdrYear: year,
    numOfRows: '1',
    pageNo: '1',
    type: 'json',
  });

  const resp = await fetch(`${endpoint}?${params}`);
  const data = await resp.json();
  const item = data?.response?.body?.items?.item?.[0];
  if (!item) throw new Error('개별주택가격 정보를 찾을 수 없습니다. 지번을 확인하세요.');
  return {
    type: 'house',
    year,
    stdValue: Number(String(item.housePc || '0').replace(/,/g, '')),
    unit: '원',
    label: '개별주택가격',
    pnu,
  };
}

/* ── 개별공시지가 ── */
async function fetchLandPrice(key, legalDongCd, jibun, year) {
  const pnu = buildPnu(legalDongCd, jibun);
  const endpoint = 'https://apis.data.go.kr/1611000/nsdi/IndLandCharInfoService/attr/getIndLandCharInfo';
  const params = new URLSearchParams({
    serviceKey: key,
    pnu,
    stdrYear: year,
    numOfRows: '1',
    pageNo: '1',
    type: 'json',
  });

  const resp = await fetch(`${endpoint}?${params}`);
  const data = await resp.json();
  const item = data?.response?.body?.items?.item?.[0];
  if (!item) throw new Error('개별공시지가 정보를 찾을 수 없습니다. 지번을 확인하세요.');
  return {
    type: 'land',
    year,
    stdValue: Number(String(item.pblntfPclnd || '0').replace(/,/g, '')),
    unit: '원/㎡',
    label: '개별공시지가',
    pnu,
    /* 토지는 지가 × 면적 = 시가표준액. 면적은 사용자 입력 필요 */
    needArea: true,
  };
}

/* ── PNU 생성: 법정동코드(10) + 산여부(1) + 번(4) + 지(4) ── */
function buildPnu(legalDongCd, jibun) {
  const code10 = legalDongCd.padEnd(10, '0').slice(0, 10);
  const parts = (jibun || '0').split('-');
  const bun = String(parts[0] || 0).replace(/[^0-9]/g, '').padStart(4, '0');
  const ji = String(parts[1] || 0).replace(/[^0-9]/g, '').padStart(4, '0');
  const san = jibun.includes('산') ? '2' : '1';   // 산번지=2, 대지=1
  return `${code10}${san}${bun}${ji}`;
}

function mockStdValue(type) {
  if (type === 'apt') return 350000000;    // 3.5억 (예시)
  if (type === 'house') return 280000000;  // 2.8억 (예시)
  return 850000;                           // 85만원/㎡ (토지, 면적 별도)
}

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' },
  });
}
