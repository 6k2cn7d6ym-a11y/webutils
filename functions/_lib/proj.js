/**
 * EPSG:5179 (Korea 2000 / Unified CS, UTMK) TM 역투영 → WGS84
 * juso.go.kr addrCoordApi.do 응답 좌표 변환용.
 *
 * GRS80: a=6,378,137, f=1/298.257222101
 * CM=127.5°E, Origin=38°N, Scale=0.9996, FE=1,000,000, FN=2,000,000
 * 정확도: 한국 범위 내 < 1 cm
 */
export function utmk5179ToWGS84(easting, northing) {
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
    + (151*e1cu/96)              * Math.sin(6*mu)
    + (1097*e1qu/512)            * Math.sin(8*mu);

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
    - (5 + 3*T1 + 10*C1 - 4*C1*C1 - 9*ep2)                  * D4/24
    + (61 + 90*T1 + 298*C1 + 45*T1*T1 - 252*ep2 - 3*C1*C1)  * D6/720
  );

  const lon = lon0 + (
    D
    - (1 + 2*T1 + C1)                                          * D3/6
    + (5 - 2*C1 + 28*T1 - 3*C1*C1 + 8*ep2 + 24*T1*T1)       * D5/120
  ) / cosP;

  return { lat: lat*RAD, lon: lon*RAD };
}
