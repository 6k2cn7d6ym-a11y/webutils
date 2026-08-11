#!/bin/bash
# 2026-08-12 웹유틸 사이클 보고서 조립 · 사마의
set -e

BASE="/Users/jim/projects/webutils/2026-08-12"
OUT_LOCAL="$BASE/04-보고서.html"
OUT_OUTBOX_DIR="/Users/jim/projects/webutils/_outbox"
OUT_OUTBOX="$OUT_OUTBOX_DIR/webutils_보고서_2026-08-12.html"

SUNEUNG_B64=$(base64 -i "$BASE/suneung-dday/index.html" | tr -d '\n')
DEFECT_B64=$(base64 -i "$BASE/defect-warranty-dday/index.html" | tr -d '\n')

mkdir -p "$OUT_OUTBOX_DIR"

cat > "$OUT_LOCAL" << HTMLEOF
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>웹유틸 2026-08-12 사이클 보고서 · 사마의</title>
<style>
  * { box-sizing: border-box; }
  body {
    margin: 0; padding: 32px 20px 80px;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Pretendard Variable', system-ui, sans-serif;
    background: #F7F8FA; color: #1a1a2e;
    -webkit-font-smoothing: antialiased;
  }
  main { max-width: 960px; margin: 0 auto; }
  h1 { font-size: 1.6rem; font-weight: 800; margin: 0 0 6px; letter-spacing: -0.03em; }
  .subtitle { color: #6c757d; font-size: 14px; margin: 0 0 32px; }
  h2 { font-size: 1.15rem; font-weight: 800; margin: 40px 0 14px; letter-spacing: -0.02em; padding-bottom: 8px; border-bottom: 2px solid #212529; }
  h3 { font-size: 1rem; font-weight: 700; margin: 24px 0 10px; letter-spacing: -0.015em; }
  .card {
    background: #fff; border: 1px solid #dee2e6; border-radius: 12px;
    padding: 22px 24px; margin-bottom: 16px;
  }
  .summary-grid {
    display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px;
    margin-bottom: 24px;
  }
  .summary-cell {
    background: #fff; border: 1px solid #dee2e6; border-radius: 10px;
    padding: 18px 16px; text-align: center;
  }
  .summary-cell .num { font-size: 2rem; font-weight: 900; letter-spacing: -0.04em; margin-bottom: 4px; }
  .summary-cell .label { font-size: 12px; color: #6c757d; font-weight: 600; letter-spacing: 0.02em; }
  .num.ok { color: #198754; }
  .num.warn { color: #fd7e14; }
  .num.info { color: #4F46E5; }
  table { width: 100%; border-collapse: collapse; font-size: 14px; margin: 8px 0 4px; }
  th {
    background: #f1f3f5; padding: 10px 12px; text-align: left;
    font-size: 12px; font-weight: 700; color: #495057;
    border-bottom: 1px solid #dee2e6;
  }
  td {
    padding: 12px; border-bottom: 1px solid #f1f3f5;
    color: #343a40; vertical-align: top; line-height: 1.55;
  }
  tr:last-child td { border-bottom: none; }
  .badge {
    display: inline-block; padding: 2px 8px; border-radius: 999px;
    font-size: 11px; font-weight: 700; letter-spacing: 0.02em;
  }
  .badge.ok { background: #D1FAE5; color: #198754; }
  .badge.fix { background: #FEF3C7; color: #B45309; }
  .badge.pending { background: #E0E7FF; color: #3730A3; }
  .badge.info { background: #F3F4F6; color: #495057; }
  .decision-card {
    background: #FFFBEB; border: 1px solid #FCD34D; border-radius: 12px;
    padding: 20px 22px; margin: 12px 0 20px;
  }
  .decision-card h3 { margin-top: 0; color: #92400E; }
  .decision-card ul { margin: 8px 0 0; padding-left: 20px; line-height: 1.75; }
  .decision-card li { margin-bottom: 4px; }
  .util-block { margin: 32px 0 40px; }
  .util-header {
    display: flex; justify-content: space-between; align-items: baseline;
    padding: 14px 18px; border-radius: 12px 12px 0 0;
    border: 1px solid #dee2e6; border-bottom: none; background: #fff;
  }
  .util-header .name { font-weight: 800; font-size: 1.05rem; letter-spacing: -0.015em; }
  .util-header .slug { font-size: 12px; color: #6c757d; font-family: ui-monospace, SFMono-Regular, monospace; }
  .util-meta {
    background: #F8F9FA; border-left: 1px solid #dee2e6; border-right: 1px solid #dee2e6;
    padding: 12px 18px; font-size: 13px; color: #495057; display: flex; gap: 16px; flex-wrap: wrap;
  }
  .util-meta span { display: inline-flex; align-items: center; gap: 4px; }
  .util-meta strong { color: #212529; font-weight: 700; }
  .preview-wrap {
    border: 1px solid #dee2e6; border-top: none; border-radius: 0 0 12px 12px;
    background: #fff; padding: 0; overflow: hidden;
  }
  iframe.preview {
    width: 100%; height: 720px; border: 0; display: block;
    background: #fff;
  }
  .checks-grid {
    display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px;
    margin-top: 12px;
  }
  .check-row {
    display: flex; justify-content: space-between; align-items: center;
    padding: 10px 14px; background: #F8F9FA; border-radius: 8px;
    font-size: 13px;
  }
  .check-row .k { color: #495057; font-weight: 600; }
  .issue-list { margin: 0; padding-left: 20px; line-height: 1.75; }
  .issue-list li { margin-bottom: 6px; }
  .kv-list { list-style: none; padding: 0; margin: 0; }
  .kv-list li {
    display: flex; gap: 12px; padding: 8px 0; border-bottom: 1px solid #f1f3f5;
    font-size: 14px;
  }
  .kv-list li:last-child { border-bottom: none; }
  .kv-list .k { min-width: 130px; color: #6c757d; font-weight: 600; }
  .kv-list .v { color: #343a40; flex: 1; }
  .foot {
    margin-top: 60px; padding-top: 20px; border-top: 1px solid #dee2e6;
    font-size: 12px; color: #adb5bd; text-align: center;
  }
  code {
    font-family: ui-monospace, SFMono-Regular, monospace; font-size: 12.5px;
    background: #F3F4F6; padding: 1px 6px; border-radius: 4px; color: #B45309;
  }
  .note { font-size: 12px; color: #6c757d; margin: 6px 0 0; line-height: 1.55; }
  @media (max-width: 640px) {
    .summary-grid { grid-template-columns: 1fr; }
    .checks-grid { grid-template-columns: 1fr; }
    iframe.preview { height: 560px; }
  }
</style>
</head>
<body>
<main>

  <h1>웹유틸 2026-08-12 사이클 보고서</h1>
  <p class="subtitle">기획전략실 팀장 · 사마의 · 2026년 8월 12일 수요일 · AdSense 심사 D-23</p>

  <div class="summary-grid">
    <div class="summary-cell">
      <div class="num info">2</div>
      <div class="label">오늘 사이클 산출</div>
    </div>
    <div class="summary-cell">
      <div class="num ok">2</div>
      <div class="label">배포 준비 완료</div>
    </div>
    <div class="summary-cell">
      <div class="num warn">0</div>
      <div class="label">조정 필요</div>
    </div>
  </div>

  <div class="decision-card">
    <h3>대표 결정 요청</h3>
    <ul>
      <li><strong>배포 실행</strong>: 2건 모두 배포 준비 완료 · 클레버 검수 통과(1건 오류 정정 반영 완료) · <strong>배포 지시 대기</strong></li>
      <li><strong>실행 스크립트</strong>: 두 폴더 <code>2026-08-12/{slug}/</code> → 루트 <code>webutils/{slug}/</code> <code>git mv</code> · <code>webutils/index.html</code> 랜딩 카드 2건 추가(자주·그린 톤) · commit + push origin main</li>
      <li><strong>광고 슬롯 형식</strong>: 두 파일 모두 옛 형식 <code>&lt;div id="ad-slot"&gt;광고&lt;/div&gt;</code>로 산출됨 (chuseok-ktx·work-grant 배포 2건과 동일 문제) · 개발팀 정합 자율지시가 진행 중이므로 <strong>같은 정합 스크립트에 이번 2건도 포함</strong> 권고 · 대표 승인 시 사마의가 자율지시 스코프 확장 통지</li>
      <li><strong>GSC 색인 요청</strong>: 배포 확정 시 오늘 대표 액션 10건 우선순위에 두 URL 반영 필요</li>
    </ul>
  </div>

  <h2>클레버 검수 결과 (4축 요약)</h2>
  <div class="card">
    <table>
      <thead>
        <tr><th style="width:120px">검수 축</th><th>결과</th><th>비고</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="badge fix">수정 1건</span></td>
          <td><strong>정확성</strong></td>
          <td>suneung-dday 학년도 표기 오류 <code>2026학년도</code> → <code>2027학년도</code> 6곳 일괄 정정 (관행상 시행 다음 해 대학 입학 학년도) · 정정 완료 · 인라인 주석 표시</td>
        </tr>
        <tr>
          <td><span class="badge ok">OK</span></td>
          <td><strong>완성도</strong></td>
          <td>2건 모두 히어로·시간표/폼·정보 카드·공유/계산 인터랙션·접근성(<code>role="alert"</code>·<code>aria-label</code>)·반응형(480px) 완비</td>
        </tr>
        <tr>
          <td><span class="badge ok">OK</span></td>
          <td><strong>원칙</strong></td>
          <td>정적 HTML · Pretendard Variable · 공통 스택(:root 8토큰·hero-line·fadeUp·hover shadow) · 다빈치 팔레트 승계(자주 <code>#6D28D9</code> · 그린 <code>#198754</code>) · 대비 5.44 / 6.46 / 7.37 (WCAG AA)</td>
        </tr>
        <tr>
          <td><span class="badge ok">OK</span></td>
          <td><strong>배포준비</strong></td>
          <td>SEO 메타·OG·Twitter·JSON-LD·canonical 전수 · Cloudflare Analytics beacon 유지 · JS 계산 로직 검증 완료 · <code>git push</code>·폴더 이동은 대표 지시 대기 (<code>_COMMON.md §7</code> 준수)</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h2>사이클 중 이슈</h2>
  <div class="card">
    <ul class="issue-list">
      <li><strong>광고 슬롯 형식 이월</strong> — 두 산출물 모두 <code>&lt;div id="ad-slot"&gt;광고&lt;/div&gt;</code> 옛 형식 · <code>&lt;ins class="adsbygoogle"&gt;</code> 컨테이너 없음 · 8/10 배포 2건과 동일 문제 · <strong>개발팀 자율지시 진행 중인 정합 작업 스코프에 포함 권고</strong></li>
      <li><strong>배포 20건 명단 재확인</strong> — 00-유틸후보.md 상단 명단에 오늘 2건 미포함(현재 20건 = 오늘 이전 · 배포 확정 시 22건). 다음 사이클 수집 세션에 갱신 통지.</li>
      <li><strong>배포 순서 권고 vs 실제 창</strong> — 벤 판정 권고("8/17~19 수능 · 8/20~22 하자보수")는 조기 배포 판단 시 조정 대상. 심사 D-23 창 앞당김 실행이 배정 근거였으므로 오늘·모레 배포도 정합. 대표 결정 대기.</li>
    </ul>
  </div>

  <h2>오늘 사이클 산출 실물 (2건)</h2>

  <div class="util-block">
    <div class="util-header">
      <div>
        <div class="name">① 2026 수능 D-day 카운터</div>
        <div class="slug">webutils/2026-08-12/suneung-dday/index.html</div>
      </div>
      <span class="badge ok">배포 준비 완료</span>
    </div>
    <div class="util-meta">
      <span>🎯 <strong>타깃</strong> 2026-11-12 (목) 1교시 08:40 KST</span>
      <span>🎨 <strong>팔레트</strong> 자주 #6D28D9 (준비·집중)</span>
      <span>🔢 <strong>D-day</strong> D-92</span>
      <span>🏷️ <strong>축</strong> 교육 시류 신규</span>
    </div>
    <div class="preview-wrap">
      <iframe class="preview" src="data:text/html;base64,${SUNEUNG_B64}" title="suneung-dday 실물 미리보기" loading="lazy"></iframe>
    </div>
    <div class="checks-grid">
      <div class="check-row"><span class="k">JS 초 단위 갱신</span><span class="badge ok">확증</span></div>
      <div class="check-row"><span class="k">공유(navigator.share + clipboard)</span><span class="badge ok">확증</span></div>
      <div class="check-row"><span class="k">학년도 표기 정정 6곳</span><span class="badge ok">반영</span></div>
      <div class="check-row"><span class="k">광고 슬롯 형식</span><span class="badge fix">옛 형식 · 정합 필요</span></div>
    </div>
  </div>

  <div class="util-block">
    <div class="util-header">
      <div>
        <div class="name">② 하자보수 청구 기한 D-day 계산기</div>
        <div class="slug">webutils/2026-08-12/defect-warranty-dday/index.html</div>
      </div>
      <span class="badge ok">배포 준비 완료</span>
    </div>
    <div class="util-meta">
      <span>🎯 <strong>타깃</strong> 공동주택관리법 시행령 별표 4 (10·5·3·2년)</span>
      <span>🎨 <strong>팔레트</strong> 그린 #198754 (권리·신뢰)</span>
      <span>🔢 <strong>산출</strong> 입주일 → 4단계 만료일·D-day</span>
      <span>🏷️ <strong>축</strong> 부동산 사후관리 (세트 검색 흡수)</span>
    </div>
    <div class="preview-wrap">
      <iframe class="preview" src="data:text/html;base64,${DEFECT_B64}" title="defect-warranty-dday 실물 미리보기" loading="lazy"></iframe>
    </div>
    <div class="checks-grid">
      <div class="check-row"><span class="k">4단계 D-day 계산·색상 분류</span><span class="badge ok">확증</span></div>
      <div class="check-row"><span class="k">입력 검증·Enter 지원·role="alert"</span><span class="badge ok">확증</span></div>
      <div class="check-row"><span class="k">.dday-cell.far 중성회색 #495057</span><span class="badge ok">반영</span></div>
      <div class="check-row"><span class="k">광고 슬롯 형식</span><span class="badge fix">옛 형식 · 정합 필요</span></div>
    </div>
  </div>

  <h2>부록 · 수집·SEO 판정 요지</h2>
  <div class="card">
    <ul class="kv-list">
      <li><span class="k">스코프</span><span class="v">AdSense 심사 대기 D-23 · 정합 안전 우선 · 9월 초·중순~11월 초 배포용 신규 발굴 · 초안 15건 → 최종 2건</span></li>
      <li><span class="k">1순위 근거</span><span class="v">수능 D-day: 시류 High +3 · 경쟁 파편화 낮음 +2 · 총 <strong>+5</strong> · D-92 매일 재방문 계측 확실</span></li>
      <li><span class="k">2순위 근거</span><span class="v">하자보수 D-day: Mid +1 + 세트 검색 흡수 보너스 +2 · 경쟁 낮음 +2 · 총 <strong>+5</strong> · 부동산 사후관리 축 3중 배포 확립</span></li>
      <li><span class="k">컷 13건</span><span class="v">개천절·한글날·김장·전세갱신·확정일자·잔금·자동차검사·종소세·김영란법·인터넷약정·근로계약서·이사후·첫서리 · 스코프 카니벌·관보대기·축 과집중·다음 사이클 배정 사유별 컷</span></li>
      <li><span class="k">이월 이슈</span><span class="v">공통 <code>ddayText(0) === 0</code> 데드코드 · <code>Math.ceil</code> 자정 인근 소소한 정밀도 · suneung 시험 시간표 평가원 공지 후 유지보수</span></li>
    </ul>
  </div>

  <div class="foot">
    작성: 사마의 (기획전략실 팀장) · 2026-08-12 07:30 KST · 로컬 아카이브 <code>webutils/2026-08-12/04-보고서.html</code>
  </div>

</main>
</body>
</html>
HTMLEOF

cp "$OUT_LOCAL" "$OUT_OUTBOX"
LOCAL_KB=$(wc -c < "$OUT_LOCAL" | awk '{printf "%.1f", $1/1024}')
OUTBOX_KB=$(wc -c < "$OUT_OUTBOX" | awk '{printf "%.1f", $1/1024}')
echo "OK · local=${LOCAL_KB}KB · outbox=${OUTBOX_KB}KB"
