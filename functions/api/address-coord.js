/**
 * GET /api/address-coord?admCd=...&rnMgtSn=...&udrtYn=...&buldMnnm=...&buldSlno=...
 * juso.go.kr 좌표제공서비스 프록시
 * ENV: JUSO_API_KEY2 — Cloudflare Pages > Settings > Environment Variables (Encrypted)
 *
 * address-search.js 결과에서 lon/lat 빈값일 때 이 엔드포인트로 보완 요청.
 * 입력 파라미터는 addrLinkApi.do 응답의 동명 필드 그대로 전달.
 */
export async function onRequestGet(context) {
  const { request, env } = context;
  const url = new URL(request.url);

  const admCd    = (url.searchParams.get('admCd')    || '').trim();
  const rnMgtSn  = (url.searchParams.get('rnMgtSn')  || '').trim();
  const udrtYn   = (url.searchParams.get('udrtYn')   || '0').trim();
  const buldMnnm = (url.searchParams.get('buldMnnm') || '0').trim();
  const buldSlno = (url.searchParams.get('buldSlno') || '0').trim();

  if (!admCd || !rnMgtSn || !buldMnnm) {
    return json({ error: '필수 파라미터(admCd, rnMgtSn, buldMnnm) 누락' }, 400);
  }

  /* ── MOCK (키 미등록 시) ── */
  if (!env.JUSO_API_KEY2) {
    return json({ _mock: true, lon: '127.028423', lat: '37.498095' });
  }

  const apiUrl = new URL('https://business.juso.go.kr/addrlink/addrCoordApi.do');
  apiUrl.searchParams.set('confmKey', env.JUSO_API_KEY2);
  apiUrl.searchParams.set('admCd',    admCd);
  apiUrl.searchParams.set('rnMgtSn',  rnMgtSn);
  apiUrl.searchParams.set('udrtYn',   udrtYn);
  apiUrl.searchParams.set('buldMnnm', buldMnnm);
  apiUrl.searchParams.set('buldSlno', buldSlno);
  apiUrl.searchParams.set('resultType', 'json');

  try {
    const resp = await fetch(apiUrl.toString());
    const raw  = await resp.text();

    let data;
    try { data = JSON.parse(raw); }
    catch (_) { return json({ error: `응답 파싱 실패 (HTTP ${resp.status})`, raw: raw.slice(0, 300) }, 502); }

    const common = data?.results?.common;
    if (common?.errorCode && common.errorCode !== '0') {
      return json({ error: `juso API 오류 [${common.errorCode}] ${common.errorMessage}`, raw: data }, 502);
    }

    const juso = data?.results?.juso?.[0];
    if (!juso) {
      return json({ error: '좌표 없음 — 건물 파라미터 확인 필요', raw: data }, 404);
    }

    return json({ lon: juso.entX || '', lat: juso.entY || '' });
  } catch (e) {
    return json({ error: `좌표 조회 중 오류: ${e.message}` }, 502);
  }
}

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' },
  });
}
