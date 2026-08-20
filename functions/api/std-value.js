/**
 * GET /api/std-value?type=apt&legalDongCd=...&lnbrMnnm=...&lnbrSlno=...&jibunAddr=...&year=2026
 * VWorld 공동주택공시가격 속성조회 (NED API)
 *
 * 엔드포인트: https://api.vworld.kr/ned/data/getApartHousingPriceAttr
 * 파라미터:   pnu(19자리) = legalDongCd(10) + 지목구분(1) + lnbrMnnm(4) + lnbrSlno(4)
 * ENV:        VWORLD_KEY
 */
export async function onRequestGet(context) {
  const { request, env } = context;
  const url = new URL(request.url);

  const type        = url.searchParams.get('type')        || 'apt';
  const year        = url.searchParams.get('year')        || String(new Date().getFullYear());
  const legalDongCd = url.searchParams.get('legalDongCd') || '';
  let   lnbrMnnm    = url.searchParams.get('lnbrMnnm')    || '0';
  let   lnbrSlno    = url.searchParams.get('lnbrSlno')    || '0';
  const jibunAddr   = url.searchParams.get('jibunAddr')   || '';

  /* jibunAddr 폴백: Juso API가 lnbrMnnm을 안 주는 케이스 */
  if (lnbrMnnm === '0' && jibunAddr) {
    const lot = extractLotFromJibun(jibunAddr);
    if (lot) { lnbrMnnm = lot.mnnm; lnbrSlno = lot.slno; }
  }

  /* 인증키 미등록 시 — 서비스 준비 중 안내 */
  if (!env.VWORLD_KEY) {
    return json({ error: '공시가격 자동조회 서비스 준비 중입니다. 직접 입력란에 수동으로 입력해 주세요.' }, 503);
  }

  /* 공동주택 외 유형은 현재 미지원 */
  if (type !== 'apt') {
    return json({ error: '현재 공동주택(아파트·연립·다세대)만 자동조회를 지원합니다. 단독주택·토지는 realtyprice.kr 또는 eum.go.kr에서 직접 확인 후 수동 입력해 주세요.' }, 400);
  }

  if (!legalDongCd || lnbrMnnm === '0') {
    return json({ error: '지번 정보를 찾을 수 없습니다. 직접 검색하여 수동 입력해 주세요.' }, 400);
  }

  /* ── PNU 조립 ── */
  const pnu = buildPnu(legalDongCd, lnbrMnnm, lnbrSlno, jibunAddr);

  /* ── 캐시 (24h) ── */
  const cacheKey = new Request(request.url);
  const cache = caches.default;
  const cached = await cache.match(cacheKey);
  if (cached) return cached;

  try {
    const u = new URL('https://api.vworld.kr/ned/data/getApartHousingPriceAttr');
    u.searchParams.set('key',      env.VWORLD_KEY);
    u.searchParams.set('pnu',      pnu);
    u.searchParams.set('stdrYear', year);
    u.searchParams.set('format',   'json');
    u.searchParams.set('numOfRows', '10');
    u.searchParams.set('pageNo',   '1');
    u.searchParams.set('domain', env.VWORLD_DOMAIN || 'utils.minon.kr');

    const domain = env.VWORLD_DOMAIN || 'utils.minon.kr';
    const resp = await fetch(u.toString(), {
      headers: { 'Referer': `https://${domain}` },
    });
    const raw  = await resp.text();

    let data;
    try { data = JSON.parse(raw); }
    catch (_) {
      return json({ error: `응답 파싱 실패 (HTTP ${resp.status}): ${raw.slice(0, 200)}` }, 502);
    }

    /* VWorld NED API 응답 구조: apartHousingPrices.items.item (배열 or 단일 객체) */
    const resultCode = data?.apartHousingPrices?.resultCode;
    if (resultCode && resultCode !== 'OK') {
      return json({ error: `VWorld 오류: ${data.apartHousingPrices.resultMsg || resultCode}` }, 502);
    }

    const rawItem = data?.apartHousingPrices?.items?.item;
    const items   = Array.isArray(rawItem) ? rawItem : (rawItem ? [rawItem] : []);

    if (!items.length) {
      return json({ error: `공시가격 정보를 찾을 수 없습니다. (pnu: ${pnu})` }, 404);
    }

    /* 첫 번째 결과 사용 */
    const props = items[0];
    const stdValue = Number(String(props.pblntfPc || 0).replace(/,/g, ''));
    if (!stdValue) {
      return json({ error: '공시가격 정보를 찾을 수 없습니다. realtyprice.kr에서 직접 확인 후 수동 입력해 주세요.' }, 404);
    }

    const result = {
      type,
      year: props.stdrYear || year,
      stdValue,
      unit: '원',
      label: '공동주택 공시가격',
      detail: [props.aphusNm, props.dongNm, props.hoNm].filter(Boolean).join(' '),
      _rawProps: props,   /* 개발 확인용 — 응답 구조 확정 후 제거 */
    };

    const response = json(result);
    const toCache  = response.clone();
    toCache.headers.set('Cache-Control', 'public, max-age=86400');
    context.waitUntil(cache.put(cacheKey, toCache));
    return response;

  } catch (e) {
    return json({ error: `공시가격 조회 중 오류: ${e.message}` }, 502);
  }
}

/**
 * PNU(19자리 부동산 고유번호) 조립
 * = 법정동코드(10) + 지목구분(1: 일반=1, 산=2) + 지번본번(4) + 지번부번(4)
 */
function buildPnu(legalDongCd, lnbrMnnm, lnbrSlno, jibunAddr) {
  const code10 = (legalDongCd || '').padEnd(10, '0').slice(0, 10);
  const bun    = String(lnbrMnnm || '0').replace(/[^0-9]/g, '').padStart(4, '0');
  const ji     = String(lnbrSlno || '0').replace(/[^0-9]/g, '').padStart(4, '0');
  const san    = (jibunAddr || '').includes('산') ? '2' : '1';
  return `${code10}${san}${bun}${ji}`;
}

/** jibunAddr 토큰에서 지번 본번·부번 추출 (예: "상일동 515" → {mnnm:'515', slno:'0'}) */
function extractLotFromJibun(jibunAddr) {
  const tokens = (jibunAddr || '').split(/\s+/);
  for (const t of tokens) {
    const m = t.match(/^(\d+)(?:-(\d+))?$/);
    if (m) return { mnnm: m[1], slno: m[2] || '0' };
  }
  return null;
}

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' },
  });
}
