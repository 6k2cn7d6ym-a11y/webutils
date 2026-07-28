/**
 * GET /api/address-search?keyword=서울 강남구 ...
 * 도로명주소 API (juso.go.kr) 프록시 + 24h 캐시
 * ENV: JUSO_API_KEY — Cloudflare Pages > Settings > Environment Variables (Encrypted)
 */
export async function onRequestGet(context) {
  const { request, env } = context;
  const url = new URL(request.url);
  const keyword = (url.searchParams.get('keyword') || '').trim();

  if (!keyword) {
    return json({ results: [] });
  }

  /* ── 캐시 (Cloudflare Cache API, 24h) ── */
  const cacheKey = new Request(request.url);
  const cache = caches.default;
  const cached = await cache.match(cacheKey);
  if (cached) return cached;

  /* ── MOCK (API 키 미등록 시) ── */
  if (!env.JUSO_API_KEY) {
    return json({
      _mock: true,
      results: [
        { roadAddr: '서울특별시 강남구 테헤란로 152', jibunAddr: '서울특별시 강남구 역삼동 737', bdNm: '강남파이낸스센터', siNm: '서울특별시', sggNm: '강남구', emdNm: '역삼동', legalDongCd: '1168010100', bdMgtSn: '1168010100107370000000001' },
        { roadAddr: '서울특별시 강남구 삼성로 212', jibunAddr: '서울특별시 강남구 대치동 888-1', bdNm: '아이파크', siNm: '서울특별시', sggNm: '강남구', emdNm: '대치동', legalDongCd: '1168010600', bdMgtSn: '1168010600108880001000001' },
      ]
    });
  }

  /* ── 실 API 호출 ── */
  const apiUrl = new URL('https://business.juso.go.kr/addrlink/addrLinkApi.do');
  apiUrl.searchParams.set('confmKey', env.JUSO_API_KEY);
  apiUrl.searchParams.set('currentPage', '1');
  apiUrl.searchParams.set('countPerPage', '10');
  apiUrl.searchParams.set('keyword', keyword);
  apiUrl.searchParams.set('resultType', 'json');

  try {
    const resp = await fetch(apiUrl.toString());
    const data = await resp.json();
    const jusoList = data?.results?.juso || [];

    const results = jusoList.map(j => ({
      roadAddr: j.roadAddr,
      jibunAddr: j.jibunAddr,
      bdNm: j.bdNm,
      siNm: j.siNm,
      sggNm: j.sggNm,
      emdNm: j.emdNm,
      legalDongCd: j.admCd,
      bdMgtSn: j.bdMgtSn,
    }));

    const response = json({ results });
    /* 캐시 저장 (24h) */
    const toCache = response.clone();
    toCache.headers.set('Cache-Control', 'public, max-age=86400');
    context.waitUntil(cache.put(cacheKey, toCache));
    return response;
  } catch (e) {
    return json({ error: '주소 검색 중 오류가 발생했습니다.', results: [] }, 502);
  }
}

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' },
  });
}
