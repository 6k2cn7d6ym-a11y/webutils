#!/usr/bin/env python3
# 보고서 조립 스크립트 · 사마의 · 2026-08-05
# 두 유틸 index.html을 iframe srcdoc용으로 escape 후 04-보고서.html + _outbox 사본 생성.
import html
import shutil
from pathlib import Path

BASE = Path("/Users/jim/projects/webutils/2026-08-05")
OUTBOX = Path("/Users/jim/projects/webutils/_outbox")
OUTBOX.mkdir(parents=True, exist_ok=True)

def load_srcdoc(p: Path) -> str:
    return html.escape(p.read_text(encoding="utf-8"), quote=True)

homework = load_srcdoc(BASE / "summer-homework-dday-calculator" / "index.html")
resident = load_srcdoc(BASE / "resident-registration-deadline" / "index.html")

REPORT = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>webutils 사이클 보고 · 2026-08-05</title>
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
  main {{ max-width: 820px; margin: 0 auto; }}
  header.top {{
    background: #1e293b;
    color: #f8fafc;
    padding: 1.5rem 1.5rem 1.75rem;
    border-radius: 12px;
    margin-bottom: 1rem;
  }}
  header.top h1 {{ font-size: 1.35rem; font-weight: 700; letter-spacing: -0.01em; }}
  header.top .meta {{ font-size: 0.85rem; color: #cbd5e1; margin-top: 0.4rem; }}
  section.card {{
    background: #fff;
    border-radius: 12px;
    padding: 1.25rem 1.5rem;
    margin-bottom: 1rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
  }}
  section.summary {{ border-left: 4px solid #10b981; }}
  h2 {{ font-size: 1.05rem; font-weight: 700; margin-bottom: 0.75rem; color: #0f172a; }}
  h3 {{ font-size: 0.95rem; font-weight: 700; margin: 1rem 0 0.5rem; color: #334155; }}
  p, li {{ font-size: 0.9rem; color: #334155; }}
  ul {{ padding-left: 1.25rem; margin: 0.35rem 0; }}
  li {{ margin-bottom: 0.2rem; }}
  .badge {{
    display: inline-block;
    padding: 0.15rem 0.55rem;
    border-radius: 999px;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.02em;
  }}
  .badge-ready {{ background: #dcfce7; color: #166534; }}
  .badge-adjust {{ background: #fef3c7; color: #92400e; }}
  .badge-block {{ background: #fee2e2; color: #b91c1c; }}
  table.tally {{
    width: 100%;
    border-collapse: collapse;
    margin-top: 0.5rem;
    font-size: 0.88rem;
  }}
  table.tally th, table.tally td {{
    padding: 0.5rem 0.65rem;
    text-align: left;
    border-bottom: 1px solid #e2e8f0;
  }}
  table.tally th {{ background: #f1f5f9; color: #475569; font-weight: 600; font-size: 0.8rem; }}
  code {{
    background: #f1f5f9;
    padding: 0.1rem 0.35rem;
    border-radius: 4px;
    font-size: 0.82rem;
    color: #0f172a;
  }}
  .util-section {{ margin-bottom: 1.25rem; }}
  .util-title {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #0f172a;
    color: #f8fafc;
    padding: 0.75rem 1rem;
    border-radius: 8px 8px 0 0;
    font-size: 0.95rem;
    font-weight: 700;
  }}
  .util-title .slug {{ font-size: 0.78rem; color: #94a3b8; font-family: 'SF Mono', Menlo, monospace; }}
  .util-frame-wrap {{
    background: #f8fafc;
    padding: 1rem;
    border-radius: 0 0 8px 8px;
    border: 1px solid #e2e8f0;
    border-top: none;
  }}
  .util-frame-wrap iframe {{
    display: block;
    width: 100%;
    height: 720px;
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    background: #fff;
  }}
  .util-frame-hint {{
    font-size: 0.78rem;
    color: #64748b;
    margin-bottom: 0.5rem;
  }}
  .decision-box {{
    background: #eff6ff;
    border: 1px solid #bfdbfe;
    border-radius: 8px;
    padding: 0.85rem 1rem;
    margin-top: 0.75rem;
  }}
  .decision-box h3 {{ margin-top: 0; color: #1e3a8a; }}
  footer.foot {{
    font-size: 0.78rem;
    color: #64748b;
    text-align: center;
    margin-top: 1rem;
  }}
</style>
</head>
<body>
<main>

<header class="top">
  <h1>webutils 사이클 보고 · 2026-08-05</h1>
  <div class="meta">기획전략실 · 사마의 · 산출 2건 · 배포 준비 완료 2건 · 조정 필요 0건</div>
</header>

<section class="card summary">
  <h2>핵심 요약</h2>
  <ul>
    <li><strong>산출 2건</strong> — 자녀 여름방학 숙제 D-day 계산기 (교육 축 신규) · 전입신고 마감일 계산기 (이사 축 신규)</li>
    <li><strong>배포 준비 완료 2건 · 조정 필요 0건</strong> — 클레버 4축 검수 통과 (정확성 수정 1건 반영 · 완성도·원칙·배포준비 OK)</li>
    <li><strong>파이프라인 정상</strong> — 마이클→피카소→달리→다빈치→클레버 순서 준수. 8/3 지적된 순서 결함 재발 없음.</li>
  </ul>
</section>

<section class="card">
  <h2>산출 유틸 목록</h2>
  <table class="tally">
    <thead>
      <tr><th>유틸명</th><th>슬러그</th><th>도메인</th><th>상태</th></tr>
    </thead>
    <tbody>
      <tr>
        <td>자녀 여름방학 숙제 D-day 계산기</td>
        <td><code>summer-homework-dday-calculator</code></td>
        <td>교육 · 개학 임박 시류</td>
        <td><span class="badge badge-ready">배포 준비</span></td>
      </tr>
      <tr>
        <td>전입신고 마감일 계산기</td>
        <td><code>resident-registration-deadline</code></td>
        <td>이사 · 행정 · 법적 기한</td>
        <td><span class="badge badge-ready">배포 준비</span></td>
      </tr>
    </tbody>
  </table>
</section>

<section class="card">
  <h2>클레버 검수 결과 (4축)</h2>
  <table class="tally">
    <thead>
      <tr><th>축</th><th>결과</th><th>세부</th></tr>
    </thead>
    <tbody>
      <tr><td>정확성</td><td>✓ 수정 1건 (반영)</td><td>summer-homework <code>err-date</code> 문구 정정 — 검증 로직과 실동작 일치</td></tr>
      <tr><td>완성도</td><td>✓ OK</td><td>Pretendard Variable · <code>:root</code> 팔레트 · h1 1.5rem · hero-line · fadeUp · 도메인별 색 정체성 (자주 vs 인디고)</td></tr>
      <tr><td>원칙</td><td>✓ OK</td><td>SEO 태그 · JSON-LD · <code>#ad-slot</code> · WCAG AA · aria-label · label for 연결</td></tr>
      <tr><td>배포준비</td><td>✓ OK</td><td>파일 규격 완결 · 이관·랜딩·push만 남음</td></tr>
    </tbody>
  </table>
  <h3>WCAG AA 대비 (다빈치 warning 격상 효과 반영)</h3>
  <ul>
    <li><strong>summer-homework</strong>: <code>#6D28D9</code> on white 7.10:1 ✓ · on soft 5.98:1 ✓ · heavy <code>#dc2626</code> on soft 4.41 (large text 통과)</li>
    <li><strong>resident-registration</strong>: <code>#4F46E5</code> on white 6.29:1 ✓ · warning <code>#92400e</code> on <code>#fffbeb</code> <strong>6.84:1</strong> ✓ (이전 <code>#f59e0b</code> 2.4:1 → 격상)</li>
  </ul>
</section>

<section class="card">
  <h2>계산·판정 로직 재검산</h2>
  <h3>summer-homework-dday-calculator</h3>
  <ul>
    <li>D-day: <code>Math.round(diffMs / 86400000)</code> · 로컬 자정 기준(<code>setHours 0,0,0,0</code>) · KST DST 없음 → 안전</li>
    <li>0-division 방지: <code>availDays = Math.max(diffDays, 1)</code> — D-DAY 케이스도 하루 할당량 계산 가능</li>
    <li>상태 분기: overdue(개학완료) / D-DAY / D-1~3(urgent) / D-4+ (basic) 정확</li>
    <li>시뮬 (오늘 2026-08-05 · 개학 2026-08-25): D-20 · 일기 15편 → 1편/하루 · 독서록 3권 → 1권/하루 ✓</li>
  </ul>
  <h3>resident-registration-deadline</h3>
  <ul>
    <li>초일 불산입: <code>new Date(vy, vm-1, vd+14)</code> — 이사 8/1 → 마감 8/15 (다음날 1일차 → 15일 14일차) 민법 원칙 준수</li>
    <li>상태 분기: overdue(&lt;0) / danger(=0, ≤3) / warning(≤7) / safe(&gt;7)</li>
    <li>진행 바 pct = (14-remainDays)/14*100 · safe만 <code>Math.max(5, pct)</code> 최소 5% 보장</li>
    <li>시뮬 (오늘 2026-08-05):
      <ul>
        <li>이사 7/22 → 마감 8/5 → remainDays=0 → danger "오늘 마감" ✓</li>
        <li>이사 7/25 → 마감 8/8 → remainDays=3 → danger D-3 (pct=78%) ✓</li>
        <li>이사 7/20 → 마감 8/3 → remainDays=-2 → overdue "2일 경과" ✓</li>
      </ul>
    </li>
    <li>move-date 기본값 오늘 자동 세팅 ✓ · JSON-LD에 주민등록법 명시 ✓</li>
  </ul>
</section>

<section class="card">
  <h2>AdSense 정합성</h2>
  <ul>
    <li>제외 카테고리(성인·의료·금융) 저촉 없음 — 교육·행정 도메인은 안전</li>
    <li><strong>카테고리 다변화</strong>: 이번 2건으로 심사 대상에 교육 축(신규) · 이사 축(진입점 확립) 추가 → 부동산 축 과집중 완화</li>
    <li>필수 페이지(privacy.html · contact.html) 리포 루트 존재 · <code>#ad-slot</code> 각 파일 상단 1개 · min-height 60px · UX 저해 없음</li>
    <li>원본 콘텐츠 · 계산·판정 로직 자체 제작 · 참고용 disclaimer(정부24 안내) 명시 → 정보성 유틸 인정 예상</li>
  </ul>
</section>

<section class="card">
  <h2>사이클 이슈</h2>
  <ul>
    <li><strong>없음</strong> — 파이프라인 정상 순서(마이클→피카소→달리→다빈치→클레버) 준수. 8/3 사이클에서 지적된 "다빈치 HTML 반영 전 클레버 검수 방 진입" 결함 재발 없음.</li>
    <li>지난 사이클(8/3) 상신 유지: (i) 4건 이관·랜딩·push 미완 (오늘 2건 포함 시 총 4건) — 개발팀 자율지시 대기 · (ii) AdSense 신청 시점 판정 대기</li>
  </ul>
</section>

<section class="card">
  <h2>대표 결정 요청</h2>
  <div class="decision-box">
    <h3>① 오늘 배포 4건 이관·랜딩·push 승인</h3>
    <p>대상: <code>apartment-subscription-score</code> · <code>apartment-subscription-special</code> (8/1) + <code>summer-homework-dday-calculator</code> · <code>resident-registration-deadline</code> (8/5) — 총 4건 (8/3 이사·기숙사 2건이 이미 오늘 이관 대기 중이면 총 6건). 개발팀(마이클·클레버) 자율지시로 30분 내 처리 가능.</p>
  </div>
  <div class="decision-box">
    <h3>② AdSense 신청 시점 판정</h3>
    <p>현재 배포 8건. 오늘 4~6건 이관 완료 시 12~14건. 신청 심사 카테고리 다변화 관점에서 오늘 이관 후 신청이 최적. 대표 승인 대기.</p>
  </div>
  <div class="decision-box">
    <h3>③ 다음 사이클(8/7) 배정 확인</h3>
    <p>수집 후보 잔여: 3(도시가스) · 6·7(부동산 사후관리 페어) · 12(추석 D-day) · 13(광복절 대체휴무 · 시류 D-10 즉효) · 9(최저임금 시류 감시) 중 최우선. 벤 실 검색량 관찰 판정 필요.</p>
  </div>
</section>

<section class="card">
  <h2>산출 유틸 실물 (인라인)</h2>
  <p class="util-frame-hint">각 유틸 index.html을 이 보고서 안에 그대로 렌더링합니다. 실제 계산·판정·상태 분기 직접 조작 가능.</p>

  <div class="util-section">
    <div class="util-title">
      <span>1. 자녀 여름방학 숙제 D-day 계산기</span>
      <span class="slug">summer-homework-dday-calculator</span>
    </div>
    <div class="util-frame-wrap">
      <iframe srcdoc="{homework}" title="방학 숙제 D-day 계산기" loading="lazy"></iframe>
    </div>
  </div>

  <div class="util-section">
    <div class="util-title">
      <span>2. 전입신고 마감일 계산기</span>
      <span class="slug">resident-registration-deadline</span>
    </div>
    <div class="util-frame-wrap">
      <iframe srcdoc="{resident}" title="전입신고 마감일 계산기" loading="lazy"></iframe>
    </div>
  </div>
</section>

<footer class="foot">
  webutils 사이클 보고 · 2026-08-05 · 기획전략실 (사마의)<br>
  로컬 아카이브: <code>webutils/2026-08-05/04-보고서.html</code> · 대표 전달: <code>_outbox/webutils_보고서_2026-08-05.html</code>
</footer>

</main>
</body>
</html>
"""

archive = BASE / "04-보고서.html"
archive.write_text(REPORT, encoding="utf-8")

outbox_copy = OUTBOX / "webutils_보고서_2026-08-05.html"
shutil.copyfile(archive, outbox_copy)

print(f"archive: {archive} · {archive.stat().st_size:,} bytes")
print(f"outbox:  {outbox_copy} · {outbox_copy.stat().st_size:,} bytes")
