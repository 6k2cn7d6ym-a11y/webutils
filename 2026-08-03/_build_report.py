#!/usr/bin/env python3
# 보고서 조립 스크립트 · 사마의 · 2026-08-03
# 두 유틸 index.html을 iframe srcdoc용으로 escape 후 04-보고서.html 생성.
# 완료 후 이 파일은 삭제한다.
import html
import shutil
from pathlib import Path

BASE = Path("/Users/jim/projects/webutils/2026-08-03")
OUTBOX = Path("/Users/jim/projects/webutils/_outbox")

def load_srcdoc(p: Path) -> str:
    return html.escape(p.read_text(encoding="utf-8"), quote=True)

moving = load_srcdoc(BASE / "moving-truck-size-calculator" / "index.html")
dorm = load_srcdoc(BASE / "dorm-vs-rent-calculator" / "index.html")

REPORT = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>webutils 사이클 보고 · 2026-08-03</title>
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
    color: #7f1d1d;
    padding: 1rem 1.25rem;
    border-radius: 8px;
    margin-bottom: 1rem;
    font-size: 0.92rem;
    line-height: 1.55;
  }}
  .verdict strong {{ color: #9f1239; }}

  section {{
    background: #fff;
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 1rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
  }}
  section h2 {{
    font-size: 1.05rem;
    font-weight: 800;
    margin-bottom: 0.85rem;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid #be123c;
    color: #1e293b;
  }}
  section h3 {{
    font-size: 0.95rem;
    font-weight: 700;
    margin: 1rem 0 0.5rem;
    color: #334155;
  }}
  section p, section li {{ font-size: 0.9rem; color: #334155; }}
  section ul {{ padding-left: 1.2rem; margin-top: 0.35rem; }}
  section li {{ margin-bottom: 0.3rem; }}

  table.util-list {{
    width: 100%;
    border-collapse: collapse;
    font-size: 0.88rem;
    margin-top: 0.5rem;
  }}
  table.util-list th, table.util-list td {{
    padding: 0.55rem 0.65rem;
    border-bottom: 1px solid #e5e7eb;
    text-align: left;
    vertical-align: top;
  }}
  table.util-list th {{
    background: #f8fafc;
    font-weight: 700;
    color: #475569;
    font-size: 0.82rem;
  }}
  table.util-list td.status {{ font-weight: 700; color: #b45309; }}
  table.util-list td code {{
    background: #f1f5f9;
    padding: 0.1rem 0.35rem;
    border-radius: 4px;
    font-size: 0.82rem;
    color: #1e293b;
  }}

  .axis-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.6rem;
    margin-top: 0.5rem;
  }}
  .axis-card {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-left: 3px solid #64748b;
    border-radius: 6px;
    padding: 0.65rem 0.8rem;
  }}
  .axis-card .name {{ font-size: 0.78rem; color: #64748b; font-weight: 700; text-transform: uppercase; letter-spacing: 0.03em; }}
  .axis-card .val {{ font-size: 0.95rem; font-weight: 700; margin-top: 0.15rem; }}
  .axis-card .val.pass {{ color: #059669; }}
  .axis-card .val.warn {{ color: #b45309; }}
  .axis-card .val.fail {{ color: #b91c1c; }}
  .axis-card .note {{ font-size: 0.78rem; color: #475569; margin-top: 0.25rem; line-height: 1.4; }}

  .decision {{
    background: #fffbeb;
    border: 1px solid #fcd34d;
    border-left: 4px solid #d97706;
    padding: 1rem 1.25rem;
    border-radius: 8px;
    margin-bottom: 1rem;
  }}
  .decision h2 {{ border: none; padding: 0; margin-bottom: 0.5rem; color: #78350f; }}
  .decision ul {{ margin-top: 0.25rem; }}
  .decision li {{ color: #78350f; margin-bottom: 0.35rem; }}

  .preview-block {{
    margin-top: 1rem;
    border: 1px solid #cbd5e1;
    border-radius: 10px;
    overflow: hidden;
    background: #fff;
  }}
  .preview-block .head {{
    background: #1e293b;
    color: #f8fafc;
    padding: 0.6rem 1rem;
    font-size: 0.85rem;
    font-weight: 700;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}
  .preview-block .head .slug {{
    font-family: 'SF Mono', Monaco, monospace;
    font-size: 0.78rem;
    color: #94a3b8;
  }}
  .preview-note {{
    background: #fef3c7;
    color: #78350f;
    padding: 0.55rem 0.9rem;
    font-size: 0.8rem;
    border-bottom: 1px solid #fcd34d;
  }}
  iframe.preview {{
    width: 100%;
    border: none;
    display: block;
    background: #f4f4f4;
  }}
  iframe.preview.moving {{ height: 1800px; }}
  iframe.preview.dorm {{ height: 1980px; }}

  code.path {{
    background: #1e293b;
    color: #f1f5f9;
    padding: 0.15rem 0.45rem;
    border-radius: 4px;
    font-size: 0.82rem;
    font-family: 'SF Mono', Monaco, monospace;
  }}
</style>
</head>
<body>
<main>

  <header class="top">
    <div class="kicker">webutils 사이클 보고</div>
    <h1>2026-08-03 (월) · 이사·개강 시류 페어 · 재작업 판단</h1>
    <div class="meta">기획전략실 · 사마의 · 산출 2건 · <strong style="color:#fca5a5">배포 불가</strong> (디자인팀 파이프라인 미완료)</div>
  </header>

  <div class="verdict">
    <strong>결론</strong>: 오늘 사이클 산출 2건 · <strong>배포 준비 완료 0건</strong> · 조정 필요 2건. 클레버 배포 불가 판정 — 디자인팀(다빈치) HTML 반영 전 클레버 검수 방이 열려 파이프라인 순서 결함 발생. Pretendard·CSS 토큰·h1 1.5rem·hero-line·확정 팔레트 모두 미반영. <strong>다빈치 재소환 → HTML 반영 → 클레버 재검수 필요</strong>.
  </div>

  <section>
    <h2>① 오늘 사이클 산출 (2건)</h2>
    <table class="util-list">
      <thead>
        <tr><th>#</th><th>유틸</th><th>슬러그</th><th>상태</th><th>조정 필요</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>1</td>
          <td>셀프 이사 짐 부피 → 트럭 크기<br><span style="font-size:0.78rem;color:#64748b">박스·가구 개수 → 부피 → 톤수 (1·1.4·2.5·5t) 매칭</span></td>
          <td><code>moving-truck-size-calculator</code></td>
          <td class="status">⚠️ 재작업</td>
          <td>디자인 미반영(티일 #0F766E) · 접근성(label 없음)</td>
        </tr>
        <tr>
          <td>2</td>
          <td>대학 기숙사 vs 자취 총비용 비교<br><span style="font-size:0.78rem;color:#64748b">지역별 기숙사비·자취 월세·공과금·식비 학기/학년 비교</span></td>
          <td><code>dorm-vs-rent-calculator</code></td>
          <td class="status">⚠️ 재작업</td>
          <td>디자인 미반영(코발트+앰버) · CSS selector 버그 클레버 수정 완료</td>
        </tr>
      </tbody>
    </table>
    <p style="font-size:0.82rem;color:#64748b;margin-top:0.5rem;padding-top:0.5rem;border-top:1px dashed #cbd5e1">
      벤 판정 근거: 시류 페어(이사 D-30~60 + 개강 D-30 절정) · 1번은 6사이클 연속 보존 · 8/1 벤 "확정 배정 권장" 명시 이행 · 5번째 축(이사) 확립.
    </p>
  </section>

  <section>
    <h2>② 클레버 4축 검수 요약</h2>
    <div class="axis-grid">
      <div class="axis-card">
        <div class="name">정확성</div>
        <div class="val pass">통과 (수정 1건)</div>
        <div class="note">dorm-vs-rent CSS selector 불일치 (.cell-dorm/.cell-rent → 실제 .dorm/.rent) 클레버 직접 수정 완료. moving-truck 계산 로직·SEO·JSON-LD 정상.</div>
      </div>
      <div class="axis-card">
        <div class="name">완성도</div>
        <div class="val fail">판단 불가</div>
        <div class="note">디자인팀 파이프라인 미완료. Pretendard·CSS 토큰·h1 1.5rem·hero-line 모두 미반영. 확정 팔레트(티일·코발트+앰버) 미적용.</div>
      </div>
      <div class="axis-card">
        <div class="name">원칙</div>
        <div class="val warn">지적 1건</div>
        <div class="note">moving-truck: .qty-val input과 가구 select에 &lt;label for&gt; 없음 · 스크린리더 접근성 미달(WCAG 1.3.1). 디자인 HTML 재작업 시 함께 처리 권고.</div>
      </div>
      <div class="axis-card">
        <div class="name">배포준비</div>
        <div class="val fail">배포 불가</div>
        <div class="note">디자인 미반영 상태로 배포 불가. 다빈치 최종 판정·HTML 반영 완료 후 클레버 재검수 필요.</div>
      </div>
    </div>
  </section>

  <section>
    <h2>③ 사이클 이슈</h2>
    <ul>
      <li><strong>[핵심] 파이프라인 순서 결함</strong> — 다빈치 HTML 반영 전 클레버 검수 방이 열림. 정상 순서는 마이클 → 피카소 → 달리 → 다빈치 → 클레버. 이번엔 달리 정리 후 다빈치·클레버가 동시 트리거된 것으로 보임. 클레버 결재 상신 (design-notes.md 하단): <em>"디자인팀 | 클레버 검수 재트리거 — 다빈치 HTML 반영 전 클레버 방이 열림 · 파이프라인 순서 조율 필요"</em></li>
      <li><strong>디자인 미반영 세부</strong> — 이사 짐: 티일 #0F766E 미적용 · 기숙사 vs 자취: 코발트 #1D4ED8 + 앰버 #D97706 미적용. 두 파일 모두 Pretendard 미도입·CSS 토큰 미선언·h1 사이즈·hero-line 없음.</li>
      <li><strong>접근성 지적 1건</strong> — moving-truck 수량 input·select에 label 미연결. 디자인 재작업 시 aria-label 또는 &lt;label for&gt; 추가 필수.</li>
      <li><strong>2026-08-01 청약 페어 배포 상태 미확인</strong> — 지난 사이클 대표 배포 판단 후속 상태 이 세션에서 확인 못함. 배포됐다면 랜딩 갱신(index.html) 여부도 병행 확인 필요.</li>
      <li><strong>7/31 pet-age-calculator-spec 워크트리 부재 지속</strong> — commit 9f16bf0 reflog·log --all에 살아있으나 워크트리에 파일 없음. 자동 스냅샷 파이프라인 결함 미조사 상태.</li>
    </ul>
  </section>

  <div class="decision">
    <h2>④ 대표 결정 요청</h2>
    <ul>
      <li><strong>디자인팀 재트리거 승인</strong> — 다빈치 최종 판정(이사 짐 티일 B안 단일 확정 승인 대기) → HTML 반영(2파일) → 클레버 재검수. 오늘 안에 재작업 가능하면 배포 재판단.</li>
      <li><strong>파이프라인 순서 규칙 재확립</strong> — 마이클(구현) → 피카소(1차 시안) → 달리(교차 검증) → <strong>다빈치(최종 판정 · HTML 반영)</strong> → 클레버(4축 검수). 클레버 트리거 조건: 다빈치 반영 완료 명시적 확인 후. 자동 파이프라인이라면 조건 훅 추가 필요.</li>
      <li><strong>배포 시점 재조정</strong> — 오늘 재작업 완료 시 8/3 배포 · 시류 대비 지연 최소. 재작업 어려우면 8/5 사이클로 이월 (시류 D-day 대비 큰 영향은 없음).</li>
      <li><strong>지난 사이클(8/1) 청약 페어 배포 상태 확인</strong> — 대표께서 배포 여부·랜딩 갱신 여부 알려주시면 다음 사이클 계획 정합 유지.</li>
      <li><strong>파이프라인 결함 (I) 조사 재상신</strong> — pet-age spec 워크트리 부재 · 자동 스냅샷이 커밋된 파일 워크트리에서 제거하는 결함 · 이번 세션도 재현 가능. 근본 조사 필요.</li>
    </ul>
  </div>

  <section>
    <h2>⑤ 유틸 실물 인라인 확인 (현재 미완성 상태 반영)</h2>
    <p style="font-size:0.85rem;color:#64748b">아래 iframe은 현재 워크트리 상태 · <strong>디자인 미반영</strong>. 계산 로직은 정상 작동. 재작업 후 최종 UI 확인 필요.</p>

    <div class="preview-block">
      <div class="head">
        <span>1. 셀프 이사 짐 부피 → 트럭 크기</span>
        <span class="slug">/moving-truck-size-calculator/</span>
      </div>
      <div class="preview-note">⚠️ 티일 #0F766E · Pretendard · hero-line · label 접근성 모두 미반영 상태</div>
      <iframe class="preview moving" srcdoc="{moving}" title="이사 짐 부피 계산기"></iframe>
    </div>

    <div class="preview-block">
      <div class="head">
        <span>2. 대학 기숙사 vs 자취 비용 비교</span>
        <span class="slug">/dorm-vs-rent-calculator/</span>
      </div>
      <div class="preview-note">⚠️ 코발트+앰버 팔레트·Pretendard·hero-line 미반영 · CSS selector 클레버 수정만 반영 상태</div>
      <iframe class="preview dorm" srcdoc="{dorm}" title="기숙사 vs 자취 비교"></iframe>
    </div>
  </section>

  <section>
    <h2>⑥ 산출 파일 경로</h2>
    <ul>
      <li><code class="path">2026-08-03/moving-truck-size-calculator/index.html</code> (21,519 bytes)</li>
      <li><code class="path">2026-08-03/dorm-vs-rent-calculator/index.html</code> (21,393 bytes)</li>
      <li><code class="path">2026-08-03/00-유틸후보.md</code> · <code class="path">2026-08-03/design-notes.md</code></li>
    </ul>
  </section>

</main>
</body>
</html>
"""

archive_path = BASE / "04-보고서.html"
archive_path.write_text(REPORT, encoding="utf-8")

OUTBOX.mkdir(exist_ok=True)
outbox_path = OUTBOX / "webutils_보고서_2026-08-03.html"
shutil.copyfile(archive_path, outbox_path)

print(f"archive: {archive_path} ({archive_path.stat().st_size:,} bytes)")
print(f"outbox:  {outbox_path} ({outbox_path.stat().st_size:,} bytes)")
