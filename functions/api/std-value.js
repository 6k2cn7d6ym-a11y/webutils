/**
 * GET /api/std-value?type=apt&year=2026&lon=...&lat=...&address=...
 * VWorld 공동주택공시가격 속성조회 프록시
 *
 * 흐름:
 *   1. juso.go.kr가 반환한 lon/lat 있으면 바로 VWorld 데이터 조회
 *   2. lon/lat 없으면 address → VWorld 지오코더 → 좌표 획득 → 데이터 조회
 *
 * ENV (Cloudflare Pages > Settings > Environment Variables, 모두 Encrypted):
 *   VWORLD_KEY  — api.vworld.kr API 키 (VWorld 신청 후 발급)
 *   JUSO_API_KEY — juso.go.kr 키 (address-search.js와 공유)
 *
 * ⚠ 레이어명(LT_C_UARPPI)과 속성명(PRC 등)은 VWorld 키 승인 후 실 문서 확인 필요
 */
export async function onRequestGet(context) {
  const { request, env } = context;
  const url = new URL(request.url);
  const type    = url.searchParams.get('type') || 'apt';
  const year    = url.searchParams.get('year') || String(new Date().getFullYear());
  const lon     = url.searchParams.get('lon') || '';      // 경도 (juso.go.kr entX)
  const lat     = url.searchParams.get('lat') || '';      // 위도 (juso.go.kr entY)
  const address = url.searchParams.get('address') || '';  // 주소 (지오코더 폴백용)

  /* ── MOCK (필수 키 미등록 시) ── */
  if (!env.VWORLD_KEY || !env.KAKAO_REST_KEY) {
    return json({
      _mock: true,
      type,
      year,
      stdValue: type === 'land' ? 850000 : type === 'apt' ? 350000000 : 280000000,
      unit: type === 'land' ? '원/㎡' : '원',
      label: type === 'land' ? '개별공시지가' : type === 'apt' ? '공동주택 공시가격' : '개별주택가격',
    });
  }

  /* ── 캐시 (24h — 공시가격은 연 1회 갱신) ── */
  const cacheKey = new Request(request.url);
  const cache = caches.default;
  const cached = await cache.match(cacheKey);
  if (cached) return cached;

  try {
    /* [1단계] 좌표 확보
     * juso addrLinkApi.do는 좌표 반환 안 함 → Kakao 지오코더 폴백
     * juso가 좌표 줄 때: geocoder 스킵 */
    let coords = { lon, lat };
    if (!lon || !lat) {
      if (!address) throw new Error('[1단계 실패] 주소 또는 좌표가 필요합니다.');
      try {
        coords = await geocode(env.KAKAO_REST_KEY, address);
      } catch (geoErr) {
        throw new Error(`[1단계 Kakao 지오코더 실패] ${geoErr.message}`);
      }
    }

    /* [2단계] VWorld 공동주택공시가격 속성 조회 */
    let result;
    try {
      result = await fetchVWorldPrice(env.VWORLD_KEY, coords, year, type);
    } catch (dataErr) {
      throw new Error(`[2단계 데이터 API 실패] ${dataErr.message}`);
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

/* ── Kakao 지오코더: 주소 → 좌표 ── */
async function geocode(kakaoKey, address) {
  const u = new URL('https://dapi.kakao.com/v2/local/search/address.json');
  u.searchParams.set('query', address);

  const resp = await fetch(u.toString(), {
    headers: { Authorization: `KakaoAK ${kakaoKey}` },
  });
  const raw = await resp.text();

  let data;
  try { data = JSON.parse(raw); }
  catch (_) { throw new Error(`Kakao 지오코더 파싱 실패 (HTTP ${resp.status}): ${raw.slice(0, 500)}`); }

  const doc = data?.documents?.[0];
  if (!doc) throw new Error(`Kakao 지오코더 좌표 없음 (HTTP ${resp.status}). 응답: ${JSON.stringify(data).slice(0, 500)}`);
  return { lon: doc.x, lat: doc.y };   /* x=경도, y=위도 (WGS84) */
}

/* ── VWorld 지오코더 (주석 보존 — 권한 확인 후 되살릴 여지) ──
async function geocodeVWorld(key, address) {
  const u = new URL('https://api.vworld.kr/req/address');
  u.searchParams.set('service', 'address');
  u.searchParams.set('request', 'getcoord');
  u.searchParams.set('address', address);
  u.searchParams.set('type', 'road');
  u.searchParams.set('key', key);
  u.searchParams.set('format', 'json');
  u.searchParams.set('crs', 'EPSG:4326');
  const resp = await fetch(u.toString());
  const raw = await resp.text();
  let data; try { data = JSON.parse(raw); } catch(_) { throw new Error(`VWorld 지오코더 파싱 실패 (HTTP ${resp.status}): ${raw.slice(0,500)}`); }
  const point = data?.response?.result?.point;
  if (!point) throw new Error(`VWorld 지오코더 좌표 없음. 응답: ${JSON.stringify(data).slice(0,500)}`);
  return { lon: point.x, lat: point.y };
}
── */

/* ── VWorld 공동주택공시가격 속성 조회 ── */
async function fetchVWorldPrice(key, { lon, lat }, year, type) {
  /* ⚠ 레이어명은 VWorld 승인 후 실제 문서에서 확인 필요 */
  const layer = 'LT_C_UARPPI';

  const u = new URL('https://api.vworld.kr/req/data');
  u.searchParams.set('service', 'data');
  u.searchParams.set('request', 'GetFeature');
  u.searchParams.set('data', layer);
  u.searchParams.set('key', key);
  u.searchParams.set('geomFilter', `POINT(${lon} ${lat})`);
  u.searchParams.set('crs', 'EPSG:4326');
  u.searchParams.set('format', 'json');
  u.searchParams.set('size', '5');
  if (year) u.searchParams.set('year', year);

  const resp = await fetch(u.toString());
  const raw = await resp.text();

  let data;
  try { data = JSON.parse(raw); }
  catch (_) { throw new Error(`VWorld 데이터 API 응답 파싱 실패 (HTTP ${resp.status}): ${raw.slice(0, 200)}`); }

  const features = data?.response?.result?.featureCollection?.features;
  if (!features?.length) {
    throw new Error('해당 위치의 공동주택 공시가격 정보를 찾을 수 없습니다. 주소가 공동주택(아파트·연립·다세대) 위치인지 확인하세요.');
  }

  const props = features[0].properties;
  /* 속성명 pblntfPc 확인됨 (공시가격 원) · 2026-07-28 대표 VWorld 문서에서 확인 */
  const stdValue = Number(
    String(props.pblntfPc || props.PRC || props.PRICE || props.price || 0).replace(/,/g, '')
  );

  return {
    type,
    year,
    stdValue,
    unit: '원',
    label: '공동주택 공시가격',
    detail: props.APT_NM || props.aptNm || props.BLDNM || '',
    rawProps: props,   // 개발 확인용 — 속성명 확정 후 제거
  };
}

/* ────────────────────────────────────────────────────────
   구 PNU 기반 코드 (주석 처리)
   개별주택가격·개별공시지가 API 추가 시 참조
────────────────────────────────────────────────────────
async function fetchAptPrice_legacy(key, legalDongCd, bdMgtSn, year) {
  const lawd_cd = legalDongCd.slice(0, 5);
  const endpoint = 'https://apis.data.go.kr/1611000/AptPriceInfo/getAptPriceInfo';
  const params = new URLSearchParams({ serviceKey: key, LAWD_CD: lawd_cd, DEAL_YMD: `${year}01`, numOfRows: '1', pageNo: '1', type: 'json' });
  if (bdMgtSn) params.set('BLDG_MNG_NO', bdMgtSn);
  const resp = await fetch(`${endpoint}?${params}`);
  const data = await resp.json();
  const item = data?.response?.body?.items?.item?.[0];
  if (!item) throw new Error('공시가격 정보를 찾을 수 없습니다.');
  return { type: 'apt', year, stdValue: Number(String(item.pblntfPc || '0').replace(/,/g, '')), unit: '원', label: '공동주택 공시가격', detail: `${item.aptNm || ''} ${item.floor || ''}층` };
}

async function fetchHousePrice_legacy(key, legalDongCd, jibun, year) {
  const pnu = buildPnu(legalDongCd, jibun);
  const endpoint = 'https://apis.data.go.kr/1611000/IndvdHousingPriceInfo/getIndvdHousingPriceInfo';
  const params = new URLSearchParams({ serviceKey: key, pnu, stdrYear: year, numOfRows: '1', pageNo: '1', type: 'json' });
  const resp = await fetch(`${endpoint}?${params}`);
  const data = await resp.json();
  const item = data?.response?.body?.items?.item?.[0];
  if (!item) throw new Error('개별주택가격 정보를 찾을 수 없습니다.');
  return { type: 'house', year, stdValue: Number(String(item.housePc || '0').replace(/,/g, '')), unit: '원', label: '개별주택가격', pnu };
}

async function fetchLandPrice_legacy(key, legalDongCd, jibun, year) {
  const pnu = buildPnu(legalDongCd, jibun);
  const endpoint = 'https://apis.data.go.kr/1611000/nsdi/IndLandCharInfoService/attr/getIndLandCharInfo';
  const params = new URLSearchParams({ serviceKey: key, pnu, stdrYear: year, numOfRows: '1', pageNo: '1', type: 'json' });
  const resp = await fetch(`${endpoint}?${params}`);
  const data = await resp.json();
  const item = data?.response?.body?.items?.item?.[0];
  if (!item) throw new Error('개별공시지가 정보를 찾을 수 없습니다.');
  return { type: 'land', year, stdValue: Number(String(item.pblntfPclnd || '0').replace(/,/g, '')), unit: '원/㎡', label: '개별공시지가', pnu, needArea: true };
}

function buildPnu(legalDongCd, jibun) {
  const code10 = legalDongCd.padEnd(10, '0').slice(0, 10);
  const parts = (jibun || '0').split('-');
  const bun = String(parts[0] || 0).replace(/[^0-9]/g, '').padStart(4, '0');
  const ji  = String(parts[1] || 0).replace(/[^0-9]/g, '').padStart(4, '0');
  const san = jibun.includes('산') ? '2' : '1';
  return `${code10}${san}${bun}${ji}`;
}
*/

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' },
  });
}
