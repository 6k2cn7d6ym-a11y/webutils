import base64, os, shutil

with open('/Users/jim/projects/webutils/2026-07-27/acquisition-tax-calculator/index.html', 'rb') as f:
    tax_b64 = base64.b64encode(f.read()).decode('ascii')
with open('/Users/jim/projects/webutils/2026-07-27/real-estate-commission-calculator/index.html', 'rb') as f:
    com_b64 = base64.b64encode(f.read()).decode('ascii')

tmpl = """<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>webutils 사이클 보고 · 2026-07-27</title>
  <meta name="robots" content="noindex, nofollow">
  <link rel="preconnect" href="https://cdn.jsdelivr.net">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard-dynamic-subset.css">
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, 'Malgun Gothic', sans-serif;
      background: #F7F8FA;
      color: #111827;
      line-height: 1.6;
      padding: 1rem;
    }
    main { max-width: 820px; margin: 0 auto; padding: 2rem 0 4rem; }
    h1 { font-size: 1.75rem; font-weight: 700; margin-bottom: 0.4rem; }
    .date { color: #6B7280; margin-bottom: 2rem; font-size: 0.95rem; }
    h2 {
      font-size: 1.2rem;
      font-weight: 700;
      margin: 2.25rem 0 0.85rem;
      padding-top: 1.25rem;
      border-top: 1px solid #E5E7EB;
    }
    h3 { font-size: 1.05rem; font-weight: 700; margin: 1rem 0 0.5rem; }
    p { margin-bottom: 0.65rem; }
    ul { padding-left: 1.4rem; margin: 0.5rem 0 0.85rem; }
    li { margin-bottom: 0.35rem; }
    li ul { margin-top: 0.35rem; }
    code {
      background: #EEF0F3;
      padding: 0.12rem 0.35rem;
      border-radius: 3px;
      font-size: 0.88em;
      font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
    }
    .util-card {
      border: 1px solid #E5E7EB;
      border-radius: 10px;
      padding: 1.1rem 1.25rem;
      margin-bottom: 1.5rem;
      background: #fff;
    }
    .util-card h3 { margin-top: 0; }
    .util-meta { color: #6B7280; font-size: 0.9rem; margin: 0.4rem 0 0.85rem; }
    .preview-frame {
      width: 100%;
      height: 780px;
      border: 1px solid #D1D5DB;
      border-radius: 6px;
      background: #fff;
    }
    .status-ok { color: #1F7A3D; font-weight: 700; }
    .status-warn { color: #B8722A; font-weight: 700; }
    .status-err { color: #B83A28; font-weight: 700; }
    .decision-box {
      background: #FFFDF8;
      border: 2px solid #B8722A;
      border-radius: 8px;
      padding: 1rem 1.25rem;
      margin: 1.5rem 0;
    }
    .decision-box h3 { margin-top: 0; color: #B8722A; }
    .issue-box {
      background: #FFF5F3;
      border: 2px solid #B83A28;
      border-radius: 8px;
      padding: 1rem 1.25rem;
      margin: 1.5rem 0;
    }
    .issue-box h3 { margin-top: 0; color: #B83A28; }
    .note { color: #6B7280; font-size: 0.88rem; margin: 0.5rem 0 1rem; }
    strong { font-weight: 700; }
  </style>
</head>
<body>
<main>
  <h1>webutils 사이클 보고 · 2026-07-27</h1>
  <p class="date">셋째 사이클 · 부동산 매매 흐름 페어 · <span class="status-warn">배포 준비 조건부</span></p>

  <h2>산출 요약</h2>
  <p><strong>2건 · 배포 준비 조건부 (수정 반영 완료 · 대표 시각 검증 필요)</strong></p>
  <ul>
    <li><strong>부동산 취득세 계산기</strong> — 슬러그 <code>acquisition-tax-calculator</code> · 매매가·주택 수·조정지역 기준 취득세·지방교육세·농특세 합계</li>
    <li><strong>부동산 중개수수료 계산기</strong> — 슬러그 <code>real-estate-commission-calculator</code> · 매매·전세·월세 국토부 요율표 기준 상한액</li>
  </ul>
  <p><strong>페어 채택 이유</strong>: 매매 계약 흐름 자연 유입("중개수수료 얼마 → 취득세 얼마") · 둘 다 High 검색량·상시 니드 · 파일럿 지속 트래픽 확보 · 시류 의존성 없음 · 부동산 실용 계산 축 확립.</p>

  <h2>카테고리 축 3축 확보 · AdSense 진입 시점</h2>
  <p><strong>24 관혼상제 · 25 여름 에너지 · 27 부동산</strong> — 파일럿 총 6건 (배포 완료 시). CLAUDE.md 신청 조건 "3~5건 이상" 초과. <strong>27일 배포 승인 시 AdSense 신청 착수 조건 갖춤.</strong></p>

  <h2>클레버 검수 결과 (4축)</h2>
  <ul>
    <li><strong>정확성</strong>: <span class="status-warn">수정</span> — 중개수수료 임대 12억+ 요율 <code>0.008 → 0.006</code> (2021.10 국토부 개정 정확값 · 매매 12억+ 0.7%와 혼동된 것으로 추정). 취득세 지방교육세·농특세는 관례 근사값 (아래 조건 3 참조).</li>
    <li><strong>완성도</strong>: <span class="status-warn">수정</span> — 두 파일 <strong>전면 재작성</strong>. 디자인팀 지시(포레스트 그린·딥 티얼 팔레트 · Pretendard CDN + preconnect · <code>:root</code> custom properties · <code>hero-line</code> · <code>resultReveal</code> keyframe · rich hover · rounded 12px 결과 카드 · select chevron 티얼 SVG 스트로크) 스펙 그대로 반영. 마이클 원본 계산 JS·SEO·<code>ad-slot</code>·form 구조는 유지.</li>
    <li><strong>원칙</strong>: <span class="status-warn">수정</span> — <code>&lt;link rel="canonical"&gt;</code> · <code>&lt;meta name="twitter:card"&gt;</code> · Pretendard preconnect 클레버 보완. disclaimer에 "2026년 기준" 정책 승계.</li>
    <li><strong>배포 준비</strong>: <span class="status-warn">조건부</span> — 아래 3조건.</li>
  </ul>

  <div class="issue-box">
    <h3>반복 이슈 · 필독 · 파이프라인 위반 2사이클 연속</h3>
    <p><strong>디자인팀 자율지시 25일 · 27일 2사이클 연속 미실행.</strong></p>
    <ul>
      <li>25일: 마이클 초안 → 클레버가 어제(24일) 팔레트 급히 이식.</li>
      <li>27일: 다빈치·달리·피카소 산출 <code>(대기)</code> 상태 · 클레버가 <code>design-notes.md</code> 지시 문서(17개 항목 + 다빈치 보완)를 발견해 <strong>직접 반영</strong>. 명의는 클레버 · 디자인팀 사후 승인 필요.</li>
    </ul>
    <p><strong>사마의 판정</strong>: 3사이클 연속 미실행 시 파이프라인 재설계 사안 자동 승격. 근본 원인은 (a) 디자인팀 자율지시가 UI에 아예 등록 안 됨 or (b) 등록됐으나 방 진입 자체가 안 일어남. <strong>대표 UI 자율지시 등록 상태 재점검 결재 필요</strong> (25일 사이클과 동일 요청 · 미해결 재상신).</p>
  </div>

  <div class="decision-box">
    <h3>대표 결정 요청</h3>
    <ul>
      <li><strong>배포 판단 · 오늘 산출 2건</strong>
        <ul>
          <li><strong>조건 1</strong>: 아래 프리뷰에서 취득세=포레스트 그린·중개수수료=딥 티얼 브랜드 시각 대조.</li>
          <li><strong>조건 2</strong>: 디자인팀(다빈치·달리·피카소) 사후 승인 요청 라운드 트리거 여부.</li>
          <li><strong>조건 3</strong>: 취득세 근사값 항목이 disclaimer로 충분히 커버되는지 대표 최종 판정.
            <ul>
              <li>지방교육세 = 취득세 × 10% (실제 표준세율에서 2% 뺀 값 기준 · 미세 차이)</li>
              <li>농어촌특별세 = 취득세 × 20% (실제 시행령과 미세 차이)</li>
              <li>1주택 6~9억 누진 공식 <code>(p×2/3 - 3)/100</code> · 2020.8 개정 이후 2주택 조정 8%·3주택+ 조정 12%·비조정 8%: 지방세법 정합</li>
            </ul>
          </li>
        </ul>
      </li>
      <li><strong>이월 배포 판단 · 4건</strong>: 07-24 <code>wedding-gift-calculator</code>·<code>funeral-condolence-calculator</code> · 07-25 <code>ac-electricity-calculator</code>·<code>studio-electricity-calculator</code> (모두 클레버 검수 완료 · 이미 루트 슬러그로 이관됨). 27일 2건과 함께 총 6건 일괄 배포? 별도 시퀀스?</li>
      <li><strong>배포 실행 지시</strong>: 승인 시 클레버에게 직접 지시로 파일 이동(<code>2026-07-27/{slug}/</code> → <code>{slug}/</code>) 및 <code>git push</code>. 현재 로컬은 origin/main보다 8커밋 앞섬(자동 스냅샷) · push 명령 필요.</li>
      <li><strong>디자인 파이프라인 결재</strong>: 자율지시 등록 상태 점검 · 3사이클 연속 미실행 시 자동 재설계 확정.</li>
      <li><strong>AdSense 신청 착수</strong>: 배포 총 6건 달성 시 신청 라운드 트리거 여부.</li>
      <li><strong>다음 사이클(07-29 수) 우선 후보 보존</strong>:
        <ul>
          <li>3번 <strong>폭염 WBGT 계산기</strong> — 폭염 시류 소멸 전 <strong>최우선</strong> (재밀림 시 완전 소멸)</li>
          <li>5번 <strong>여름 황금연차</strong> — 광복절(8/15) 임박(8/10~14) 재검토</li>
          <li>2번 <strong>전세 갱신 통보 마감일</strong> — 부동산 축 확장</li>
          <li>6+7번 <strong>강아지·고양이 나이 페어</strong> · 8번 <strong>파워 서플라이 W</strong> · 10번 <strong>청약 가점</strong> · 13번 <strong>최저임금 미달</strong> · 14번 <strong>셀프 이사 부피</strong> · 15번 <strong>기숙사 vs 자취</strong></li>
        </ul>
      </li>
    </ul>
  </div>

  <h2>유틸 실물 프리뷰</h2>
  <p class="note">각 유틸 HTML을 이 보고서 파일 안에 그대로 인라인(base64 iframe) — 이 파일 하나만으로 계산 로직·팔레트·UX 실물 확인 가능. 별도 배포 URL 없이 즉시 검증.</p>

  <div class="util-card">
    <h3>부동산 취득세 계산기 (포레스트 그린)</h3>
    <p class="util-meta">슬러그 <code>acquisition-tax-calculator</code> · 배포 예정 URL <code>https://utils.minon.kr/acquisition-tax-calculator/</code></p>
    <iframe src="data:text/html;charset=utf-8;base64,__TAX_B64__" class="preview-frame" title="부동산 취득세 계산기 프리뷰" loading="lazy"></iframe>
  </div>

  <div class="util-card">
    <h3>부동산 중개수수료 계산기 (딥 티얼)</h3>
    <p class="util-meta">슬러그 <code>real-estate-commission-calculator</code> · 배포 예정 URL <code>https://utils.minon.kr/real-estate-commission-calculator/</code></p>
    <iframe src="data:text/html;charset=utf-8;base64,__COM_B64__" class="preview-frame" title="부동산 중개수수료 계산기 프리뷰" loading="lazy"></iframe>
  </div>

</main>
</body>
</html>
"""

report = tmpl.replace("__TAX_B64__", tax_b64).replace("__COM_B64__", com_b64)

path_local = '/Users/jim/projects/webutils/2026-07-27/04-보고서.html'
path_out = '/Users/jim/projects/webutils/_outbox/webutils_보고서_2026-07-27.html'

with open(path_local, 'w', encoding='utf-8') as f:
    f.write(report)
shutil.copy(path_local, path_out)

print(f"local: {os.path.getsize(path_local)}B")
print(f"outbox: {os.path.getsize(path_out)}B")
