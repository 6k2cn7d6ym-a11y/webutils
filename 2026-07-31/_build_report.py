#!/usr/bin/env python3
# 보고서 조립 스크립트 · 사마의 · 2026-07-31
# 두 유틸 index.html을 iframe srcdoc용으로 escape 후 04-보고서.html 생성.
# 완료 후 이 파일은 삭제한다.
import html
from pathlib import Path

BASE = Path("/Users/jim/projects/webutils/2026-07-31")

def load_srcdoc(p: Path) -> str:
    return html.escape(p.read_text(encoding="utf-8"), quote=True)

apparent = load_srcdoc(BASE / "apparent-temperature-calculator" / "index.html")
holiday  = load_srcdoc(BASE / "public-holiday-substitute-2026" / "index.html")

REPORT = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>webutils 사이클 보고 · 2026-07-31</title>
<style>
  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Malgun Gothic', sans-serif;
    font-size: 15px;
    line-height: 1.65;
    color: #1a1a1a;
    background: #f5f5f7;
    padding: 1.5rem 1rem 3rem;
  }}
  main {{ max-width: 780px; margin: 0 auto; }}
  header.top {{
    background: #1e293b;
    color: #f8fafc;
    padding: 1.5rem 1.5rem 1.75rem;
    border-radius: 12px;
    margin-bottom: 1rem;
  }}
  header.top .kicker {{
    font-size: 0.78rem; letter-spacing: 0.05em; color: #94a3b8;
    text-transform: uppercase; margin-bottom: 0.35rem;
  }}
  header.top h1 {{ font-size: 1.5rem; font-weight: 800; letter-spacing: -0.01em; }}
  header.top .meta {{ font-size: 0.85rem; color: #cbd5e1; margin-top: 0.4rem; }}

  .verdict {{
    background: #fff1f2;
    border: 1px solid #fecdd3;
    border-left: 4px solid #be123c;
    border-radius: 10px;
    padding: 1rem 1.15rem;
    margin-bottom: 1rem;
  }}
  .verdict h2 {{ font-size: 0.95rem; color: #9f1239; margin-bottom: 0.35rem; }}
  .verdict p {{ font-size: 0.9rem; color: #431c1f; }}
  .verdict .num {{ font-weight: 800; }}

  .card {{
    background: #fff;
    border-radius: 10px;
    padding: 1.15rem 1.25rem;
    margin-bottom: 1rem;
    box-shadow: 0 1px 3px rgba(15, 23, 42, 0.06);
  }}
  .card h2 {{
    font-size: 1rem; font-weight: 700; margin-bottom: 0.65rem;
    padding-bottom: 0.4rem; border-bottom: 1px solid #e5e7eb;
  }}
  .card h3 {{ font-size: 0.92rem; font-weight: 700; margin: 0.9rem 0 0.35rem; }}
  .card p, .card li {{ font-size: 0.9rem; }}
  .card ul, .card ol {{ padding-left: 1.15rem; }}
  .card li {{ margin-bottom: 0.3rem; }}
  .card strong {{ color: #0f172a; }}

  .kv-table {{
    width: 100%; border-collapse: collapse; font-size: 0.88rem;
    margin-top: 0.5rem;
  }}
  .kv-table th, .kv-table td {{
    border: 1px solid #e5e7eb; padding: 0.5rem 0.7rem; text-align: left;
    vertical-align: top;
  }}
  .kv-table th {{ background: #f8fafc; font-weight: 600; width: 8rem; }}

  .status-badge {{
    display: inline-block; font-size: 0.75rem; font-weight: 700;
    padding: 0.15rem 0.55rem; border-radius: 4px; margin-left: 0.4rem;
    vertical-align: middle;
  }}
  .status-fail {{ background: #fee2e2; color: #991b1b; }}
  .status-warn {{ background: #fef3c7; color: #92400e; }}
  .status-ok   {{ background: #dcfce7; color: #166534; }}

  .util-block {{ margin-bottom: 1.25rem; }}
  .util-block h2 {{ font-size: 1.05rem; }}
  .util-slug {{ font-family: ui-monospace, 'SFMono-Regular', Menlo, monospace;
    font-size: 0.8rem; color: #64748b; margin-left: 0.4rem; }}

  .iframe-wrap {{
    margin-top: 0.65rem;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    overflow: hidden;
    background: #f4f4f4;
  }}
  .iframe-wrap iframe {{
    width: 100%;
    height: 640px;
    border: 0;
    display: block;
    background: #fff;
  }}
  .iframe-cap {{
    font-size: 0.75rem; color: #64748b; padding: 0.4rem 0.7rem;
    background: #f1f5f9; border-top: 1px solid #cbd5e1;
  }}

  .decisions {{
    background: #fffbeb; border: 1px solid #fde68a;
    border-left: 4px solid #b45309;
  }}
  .decisions h2 {{ color: #78350f; border-color: #fcd34d; }}
  .decisions ol {{ padding-left: 1.25rem; }}
  .decisions li {{ margin-bottom: 0.55rem; }}
  .decisions .ask {{ font-weight: 700; color: #78350f; }}

  .footer {{
    font-size: 0.78rem; color: #64748b; text-align: center;
    margin-top: 1.5rem; padding-top: 0.75rem;
    border-top: 1px solid #e2e8f0;
  }}

  .axis-grid {{
    display: grid; grid-template-columns: 1fr 1fr; gap: 0.55rem;
    margin-top: 0.35rem;
  }}
  .axis-cell {{
    background: #f8fafc; border-radius: 6px; padding: 0.55rem 0.7rem;
    font-size: 0.85rem;
  }}
  .axis-cell .lbl {{ font-size: 0.72rem; color: #64748b; text-transform: uppercase;
    letter-spacing: 0.03em; margin-bottom: 0.15rem; }}
  .axis-cell.ok   {{ background: #f0fdf4; }}
  .axis-cell.fix  {{ background: #fff7ed; }}
  .axis-cell.fail {{ background: #fef2f2; }}
</style>
</head>
<body>
<main>

<header class="top">
  <div class="kicker">webutils · 사이클 보고 · 5단계</div>
  <h1>2026-07-31 (금) 사이클 · 배포 불가 판정</h1>
  <div class="meta">기획전략실 팀장 사마의 · 작성 07:xx KST · 사이클 라운드 2/주</div>
</header>

<div class="verdict">
  <h2>핵심 요약 (3줄)</h2>
  <p>산출 <span class="num">2건</span> (체감온도 · 광복절 대체휴일)</p>
  <p>배포 준비 완료 <span class="num">0건</span> — 두 건 모두 배포 불가</p>
  <p>조정 필요 <span class="num">2건</span> — 디자인 왕복 미완 + 체감온도 겨울 로직 결함 + WCAG AA 대비 미달</p>
</div>

<section class="card decisions">
  <h2>대표 결정 요청</h2>
  <ol>
    <li>
      <span class="ask">다음 사이클(8/3 월) 재검수 시퀀스 승인</span> —
      피카소 → 달리 → 다빈치 왕복(디자인 33개 지시 반영) + 마이클 체감온도 겨울 진입 로직 재작업 + 클레버 재검수 4축.
      본 2건은 재검수 통과 후에만 배포 후보. 오늘 사이클 결과물은 <strong>배포 대기</strong>로 이월.
    </li>
    <li>
      <span class="ask">파이프라인 병목 진단 · 프로세스 결정</span> —
      2사이클 연속(2026-07-29 · 2026-07-31) 클레버 검수 시점에 피카소 시안 미반영 상태.
      마이클 초안 → 다빈치 색 팔레트/지시 → <strong>피카소 실행 부재</strong> → 달리 검토 부재 → 다빈치 최종 부재 → 클레버 검수 진입의 패턴이 두 번 반복.
      원인 진단·개입 판단 대표 요청 (자세한 안 아래 "시스템 이슈" 섹션).
    </li>
    <li>
      <span class="ask">AdSense 신청 임박 관점 재확인</span> —
      현재 배포 8건 · 카테고리 축 4개 확립. 오늘 페어(체감온도 · 광복절)는 5번째 축(기상·안전) + 여름 시류 마지막 흡수 목적이었으나 이월.
      다음 사이클 재검수 통과 후 배포되면 총 10건 · 5축. 신청 창구 8월 3~4일에서 <strong>8월 4~7일로 밀림 가능성</strong>.
    </li>
  </ol>
</section>

<section class="card">
  <h2>클레버 검수 · 4축 결과</h2>
  <div class="axis-grid">
    <div class="axis-cell fix">
      <div class="lbl">정확성</div>
      <strong>수정 (직접 처리 · 1건)</strong><br>
      공휴일대체 근거 법률 개정연도 오타 2022→2023 정정. 부처님오신날·크리스마스 대체휴일 편입은 2023-05 대통령령 개정이 근거이므로 리스트-근거 논리 정합.
    </div>
    <div class="axis-cell fail">
      <div class="lbl">완성도</div>
      <strong>실패 — 배포 불가</strong><br>
      디자인팀 피카소 시안 33개 지시 항목 반영 <strong>0건</strong>. 두 파일 모두 마이클 초안 그대로. 브랜드 승계 파탄.
    </div>
    <div class="axis-cell ok">
      <div class="lbl">원칙</div>
      <strong>통과</strong><br>
      SEO 태그·JSON-LD·접근성 aria·광고 슬롯·JS 문법 전부 통과. 체감온도 <code>node --check</code> PASS · 공휴일대체 JS 없음.
    </div>
    <div class="axis-cell fail">
      <div class="lbl">배포준비</div>
      <strong>배포 불가</strong><br>
      (a) 체감온도 <code>#0ea5e9</code> on white ≈ 2.7:1 · WCAG AA 4.5:1 <strong>심각 미달</strong><br>
      (b) 체감온도 겨울 진입 로직 결함 · 저온 무풍(-15℃/3km/h) 케이스 "😊 쾌적" 오판
    </div>
  </div>
</section>

<section class="card util-block">
  <h2>산출 ① 체감온도 계산기 <span class="util-slug">apparent-temperature-calculator</span> <span class="status-badge status-fail">배포 불가</span></h2>
  <table class="kv-table">
    <tr><th>목적</th><td>기온·습도·풍속 통합 체감온도 즉시 계산 (여름 Rothfusz 열지수 · 겨울 NWS 풍속냉각지수)</td></tr>
    <tr><th>배포 축</th><td>29일 WBGT와 페어 → 5번째 카테고리 축 <strong>기상·안전</strong> 확립 (신설)</td></tr>
    <tr><th>주요 이슈</th><td>
      <strong>① 디자인 미반영</strong> — 하늘 청 팔레트(<code>#0072A8</code>) · Pretendard · hero-line · CSS custom properties 등 33개 지시 항목 반영 0<br>
      <strong>② WCAG AA 심각 미달</strong> — 마이클 원본 <code>#0ea5e9</code> on white = 2.7:1 (목표 4.5:1)<br>
      <strong>③ 겨울 진입 로직 결함</strong> — <code>tc &lt;= 10 &amp;&amp; vkmh &gt;= 5</code> 조건 미충족 시 <code>formula: 'neutral'</code> → 영하 저온 무풍 케이스에서 "😊 쾌적 외출하기 좋은 날씨" 표기 (안전 신호 반대). 클레버 이월 · 다음 사이클 마이클 재작업 필수
    </td></tr>
    <tr><th>조정 후 배포 조건</th><td>피카소→달리→다빈치 왕복 완료 · 마이클 겨울 로직 재작업 · 클레버 재검수 4축 통과</td></tr>
  </table>
  <div class="iframe-wrap">
    <iframe srcdoc="{apparent}" title="체감온도 계산기 실물 프리뷰"></iframe>
    <div class="iframe-cap">현재 상태 실물 (마이클 초안 · 디자인 미반영). 로컬 경로: <code>webutils/2026-07-31/apparent-temperature-calculator/index.html</code></div>
  </div>
</section>

<section class="card util-block">
  <h2>산출 ② 광복절 대체공휴일 확인 <span class="util-slug">public-holiday-substitute-2026</span> <span class="status-badge status-fail">배포 불가</span></h2>
  <table class="kv-table">
    <tr><th>목적</th><td>2026 광복절 8/15(토) → 대체 8/17(월) 팩트 확인 + 연차 조합 시나리오 5종 + 하반기 대체공휴일 3건</td></tr>
    <tr><th>배포 축</th><td>29일 황금연차와 페어 → 광복절 D-15 시류 마지막 흡수. 검색 의도 다름("연차 조합 최적" vs "이 날 진짜 쉬나?")</td></tr>
    <tr><th>주요 이슈</th><td>
      <strong>① 디자인 미반영</strong> — 코발트 블루 팔레트 · fact-box 3단 소프트 토큰 · rule-bullet 다빈치 보완 · 인라인 style→.footnote 추출 등 반영 0<br>
      <strong>② 정확성 수정 완료</strong> — 근거 법률 2022년 개정 → <strong>2023년 개정</strong> 클레버 직접 정정 (부처님오신날·크리스마스 대체휴일 편입 근거 정합)<br>
      <strong>③ 팩트 검증 통과</strong> — 광복절 요일·대체휴일 8/17·연차 조합 5케이스(0/1/2/4/5일)·달력 요일·하반기 대체 3건 전부 Python date 대조 정확
    </td></tr>
    <tr><th>조정 후 배포 조건</th><td>피카소→달리→다빈치 왕복 완료 · 클레버 재검수 4축 통과 (겨울 로직 이슈 무관 · 디자인만 걸림)</td></tr>
  </table>
  <div class="iframe-wrap">
    <iframe srcdoc="{holiday}" title="광복절 대체공휴일 실물 프리뷰"></iframe>
    <div class="iframe-cap">현재 상태 실물 (마이클 초안 + 클레버 근거 연도 정정 · 디자인 미반영). 로컬 경로: <code>webutils/2026-07-31/public-holiday-substitute-2026/index.html</code></div>
  </div>
</section>

<section class="card">
  <h2>시스템 이슈 · 파이프라인 병목 (2사이클 연속)</h2>
  <p><strong>패턴</strong>: <code>웹유틸-디자인</code> 자율지시 방에서 다빈치(팀장)가 색 팔레트·33개 지시 항목을 제시한 뒤, 피카소(사원)의 실제 파일 반영(=시안 결과 섹션 채우기)이 이루어지지 않은 채 방이 끝나거나 이월. 결과적으로 클레버가 마이클 초안을 그대로 받아 검수하는 상태 2회 연속 재현.</p>
  <h3>클레버 소견 (design-notes.md 인용)</h3>
  <blockquote style="border-left:3px solid #cbd5e1; padding-left:0.9rem; color:#334155; font-size:0.87rem; margin:0.5rem 0;">
    "두 사이클(2026-07-29·2026-07-31) 연속으로 클레버 검수 시점에 피카소 시안 미반영 상태. 파이프라인 병목 존재 (마이클 초안 → 디자인 지시만 있고 피카소 실행이 안 됨). 클레버가 디자인 지시를 직접 코드에 붙이는 건 왕복 사이클 무력화 · 명의 사칭 소지 → 반영 안 함."
  </blockquote>
  <h3>사마의 진단 (참모 판단 · 대표 확인 필요)</h3>
  <ul>
    <li><strong>가설 A · 지시 밀도 과다</strong>: 33개 지시 항목이 피카소(Haiku)의 세션 내 처리 한도를 초과. 왕복 회차가 1/5 소진되며 시안 결과 섹션이 "(대기)" 상태로 종결. 다음 사이클 진입 시 신규 방으로 리셋되어 반영 기회 소멸. → 지시 항목을 15개 이하로 압축하거나 다빈치가 페어별로 분할 지시.</li>
    <li><strong>가설 B · 왕복 프로토콜 문제</strong>: 피카소→달리→다빈치 트리오 반려 프로토콜이 파일 상태 판단으로만 굴러가서, "피카소 실행 안 됨" 상태에서 다빈치 최종만 채워지거나 클레버가 넘겨받는 순서상 헛점 존재. → 각 페르소나가 다음 페르소나 지목 마커(<code>[[자율 지시: ...]]</code>)를 명시해서 상태 넘김 보장.</li>
    <li><strong>가설 C · 자율지시 세션 스코프 불일치</strong>: <code>웹유틸-디자인</code> 자율지시 프롬프트가 "다빈치 시안 확정"까지만 스코프로 잡혀 피카소 실행이 optional로 취급될 여지. → 프롬프트에서 "피카소가 실제 파일 수정 반영을 완료해야 방 종료 가능"을 명시.</li>
  </ul>
  <p style="margin-top:0.5rem;"><strong>사마의 권고</strong>: 가설 A·C가 결합된 원인 가능성이 높다. 다음 사이클 진입 전 <code>웹유틸-디자인</code> 자율지시 프롬프트를 대표가 <strong>(1) 33개 → 상위 10~15개 압축 기준 명시 (2) 방 종료 조건에 "피카소 시안 결과 섹션 채워짐" 명시</strong> 두 항목으로 갱신 검토. 두 가설 검증은 다음 사이클에서 결과로 확인 가능.</p>
</section>

<section class="card">
  <h2>사이클 중 이슈 · 이월 항목</h2>
  <ul>
    <li><strong>체감온도 겨울 로직 결함</strong> — 클레버 이월. 다음 사이클 마이클 재작업 대상. 개선안: <code>if (tc &lt;= 10)</code>로 완화, <code>vkmh &lt; 5</code>면 <code>windChillC</code> 대신 <code>tc</code> 그대로 반환하되 winter formula/level 태깅. 배포 전 반드시 fix.</li>
    <li><strong>인라인 style 잔존</strong> — 공휴일대체 line 243·272 두 곳. 디자인 지시 30번(<code>.footnote</code> class 추출)이 반영되면 자동 해소. 클레버 별도 수정 없음.</li>
    <li><strong>AdSense 신청 창구</strong> — 신청 예정 배포 5건 원칙 상 이번 페어 배포로 총 10건 달성 예정이었으나 이월. 다음 사이클 8/3(월) 재검수 통과 시 정확히 5축 확립 조건 성립. Kill switch 재검토 시점(9월 초)까지 여유 있음.</li>
  </ul>
</section>

<section class="card">
  <h2>다음 사이클(2026-08-03 월) 작업 시퀀스 · 대표 승인 후 진행</h2>
  <ol>
    <li><strong>피카소 실행</strong> — <code>2026-07-31/design-notes.md</code> § 피카소 구현 지시(33항) 반영. 두 index.html 실제 수정. "피카소 시안 결과" 섹션 채움.</li>
    <li><strong>마이클 겨울 로직 재작업</strong> — 체감온도 <code>calcApparent</code> 분기 조건 수정. <code>tc &lt;= 10</code>만으로 겨울 진입, 무풍시 <code>tc</code> 반환.</li>
    <li><strong>달리 검토 · 다빈치 최종</strong> — design-notes 각 섹션 채움. 시각 강도·접근성 재확인.</li>
    <li><strong>클레버 재검수</strong> — 4축 전면 재판정. 통과 시 배포 준비 완료 마킹.</li>
    <li><strong>사마의 보고 재작성 → 대표 배포 결정</strong> — 이 시퀀스 이후 배포 판정.</li>
  </ol>
  <p>병행: 다음 사이클 신규 후보 수집도 정상 진행(<code>웹유틸-수집</code>). 오늘 이월 페어는 기존 스택에 얹혀 최우선 배포 후보로 이월 처리. 신규 수집·SEO는 페어 재검수와 별도 슬롯.</p>
</section>

<div class="footer">
  기획전략실 팀장 사마의 · 2026-07-31 07:xx KST · 로컬 아카이브: <code>webutils/2026-07-31/04-보고서.html</code>
</div>

</main>
</body>
</html>
"""

out_local = BASE / "04-보고서.html"
out_outbox = Path("/Users/jim/projects/webutils/_outbox/webutils_보고서_2026-07-31.html")
out_local.write_text(REPORT, encoding="utf-8")
out_outbox.write_text(REPORT, encoding="utf-8")

print(f"local:  {out_local}  ({out_local.stat().st_size:,} bytes)")
print(f"outbox: {out_outbox}  ({out_outbox.stat().st_size:,} bytes)")
