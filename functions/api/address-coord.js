/**
 * GET /api/address-coord?admCd=...&rnMgtSn=...&udrtYn=...&buldMnnm=...&buldSlno=...
 * juso.go.kr 좌표제공서비스 프록시 + EPSG:5179→WGS84 변환
 * ENV: JUSO_API_KEY2 — 좌표제공서비스 전용 키
 *
 * addrCoordApi.do는 EPSG:5179 (UTMK, GRS80 TM) 좌표를 반환.
 * 반환 전 WGS84 (십진도) 로 변환하여 지도 API와 호환.
 *
 * 입력 파라미터는 address-search.js (addrLinkApi.do) 응답의 동명 필드 그대로.
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

  if (!env.JUSO_API_KEY2) {
    return json({ _mock: true, lon: '127.0284230', lat: '37.4980950' });
  }

  const apiUrl = new URL('https://business.juso.go.kr/addrlink/addrCoordApi.do');
  apiUrl.searchParams.set('confmKey',  env.JUSO_API_KEY2);
  apiUrl.searchParams.set('admCd',     admCd);
  apiUrl.searchParams.set('rnMgtSn',   rnMgtSn);
  apiUrl.searchParams.set('udrtYn',    udrtYn);
  apiUrl.searchParams.set('buldMnnm',  buldMnnm);
  apiUrl.searchParams.set('buldSlno',  buldSlno);
  apiUrl.searchParams.set('resultType','json');

  try {
    const resp = await fetch(apiUrl.toString());
    const raw  = await resp.text();

    let data;
    try { data = JSON.parse(raw); }
    catch (_) {
      return json({ error: `응답 파싱 실패 (HTTP ${resp.status})`, raw: raw.slice(0, 300) }, 502);
    }

    const common = data?.results?.common;
    if (common?.errorCode && common.errorCode !== '0') {
      return json({ error: `juso API 오류 [${common.errorCode}] ${common.errorMessage}`, raw: data }, 502);
    }

    const juso = data?.results?.juso?.[0];
    if (!juso) {
      return json({ error: '좌표 없음 — 건물 파라미터 확인 필요', raw: data }, 404);
    }

    const tmX = parseFloat(juso.entX);
    const tmY = parseFloat(juso.entY);
    if (!tmX || !tmY) {
      return json({ error: 'API 좌표 빈값', raw: juso }, 404);
    }

    /* addrCoordApi.do는 EPSG:5179 (UTMK) 반환 → WGS84 역투영 */
    const wgs = utmk5179ToWGS84(tmX, tmY);

    return json({
      lon: wgs.lon.toFixed(7),
      lat: wgs.lat.toFixed(7),
      _tmX: tmX,   // 디버깅용 — 확인 후 제거 가능
      _tmY: tmY,
    });
  } catch (e) {
    return json({ error: `좌표 조회 중 오류: ${e.message}` }, 502);
  }
}

/**
 * EPSG:5179 (Korea 2000 / Unified CS, UTMK) TM 역투영 → WGS84
 * GRS80: a=6,378,137, f=1/298.257222101
 * CM=127.5°E, Origin=38°N, Scale=0.9996, FE=1,000,000, FN=2,000,000
 * 정확도: 한국 범위 내 < 1 cm
 */
function utmk5179ToWGS84(easting, northing) {
  const DEG  = Math.PI / 180;
  const RAD  = 180 / Math.PI;
  const a    = 6378137.0;
  const f    = 1 / 298.257222101;
  const e2   = 2*f - f*f;
  const k0   = 0.9996;
  const lon0 = 127.5 * DEG;
  const lat0 = 38.0  * DEG;
  const FE   = 1000000.0;
  const FN   = 2000000.0;

  function mArc(phi) {
    const e4 = e2*e2, e6 = e4*e2;
    return a * (
      (1 - e2/4 - 3*e4/64 - 5*e6/256) * phi
      - (3*e2/8 + 3*e4/32 + 45*e6/1024) * Math.sin(2*phi)
      + (15*e4/256 + 45*e6/1024) * Math.sin(4*phi)
      - (35*e6/3072) * Math.sin(6*phi)
    );
  }

  const M0  = mArc(lat0);
  const x   = easting  - FE;
  const y   = northing - FN;
  const M   = M0 + y / k0;
  const mu  = M / (a * (1 - e2/4 - 3*e2*e2/64 - 5*e2*e2*e2/256));

  const e1   = (1 - Math.sqrt(1 - e2)) / (1 + Math.sqrt(1 - e2));
  const e1sq = e1*e1;
  const e1cu = e1sq*e1;
  const e1qu = e1sq*e1sq;

  const phi1 = mu
    + (3*e1/2    - 27*e1cu/32) * Math.sin(2*mu)
    + (21*e1sq/16 - 55*e1qu/32) * Math.sin(4*mu)
    + (151*e1cu/96)             * Math.sin(6*mu)
    + (1097*e1qu/512)           * Math.sin(8*mu);

  const sinP = Math.sin(phi1);
  const cosP = Math.cos(phi1);
  const tanP = sinP / cosP;
  const ep2  = e2 / (1 - e2);
  const N1   = a / Math.sqrt(1 - e2*sinP*sinP);
  const T1   = tanP*tanP;
  const C1   = ep2*cosP*cosP;
  const R1   = a*(1-e2) / Math.pow(1 - e2*sinP*sinP, 1.5);
  const D    = x / (N1*k0);
  const D2 = D*D, D3 = D2*D, D4 = D2*D2, D5 = D4*D, D6 = D4*D2;

  const lat = phi1 - (N1*tanP/R1) * (
    D2/2
    - (5 + 3*T1 + 10*C1 - 4*C1*C1 - 9*ep2)                           * D4/24
    + (61 + 90*T1 + 298*C1 + 45*T1*T1 - 252*ep2 - 3*C1*C1)           * D6/720
  );

  const lon = lon0 + (
    D
    - (1 + 2*T1 + C1)                                                   * D3/6
    + (5 - 2*C1 + 28*T1 - 3*C1*C1 + 8*ep2 + 24*T1*T1)                * D5/120
  ) / cosP;

  return { lat: lat*RAD, lon: lon*RAD };
}

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' },
  });
}
