#!/usr/bin/env python3
# 보고서 조립 스크립트 · 사마의 · 2026-08-01
# 두 유틸 index.html을 iframe srcdoc용으로 escape 후 04-보고서.html 생성.
# 완료 후 이 파일은 삭제한다.
import html
import shutil
from pathlib import Path

BASE = Path("/Users/jim/projects/webutils/2026-08-01")
OUTBOX = Path("/Users/jim/projects/webutils/_outbox")

def load_srcdoc(p: Path) -> str:
    return html.escape(p.read_text(encoding="utf-8"), quote=True)

score = load_srcdoc(BASE / "apartment-subscription-score" / "index.html")
special = load_srcdoc(BASE / "apartment-subscription-special" / "index.html")

REPORT = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>webutils 사이클 보고 · 2026-08-01</title>
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
    background: #ecfdf5;
    border: 1px solid #a7f3d0;
    border-left: 4px solid #059669;
    color: #064e3b;
    padding: 1rem 1.25rem;
    border-radius: 8px;
    margin-bottom: 1rem;
    font-size: 0.92rem;
    line-height: 1.55;
  }}
  .verdict strong {{ color: #047857; }}

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
    border-bottom: 2px solid #1D4ED8;
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
  table.util-list td.status {{ font-weight: 700; color: #059669; }}
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
    border-left: 3px solid #1D4ED8;
    border-radius: 6px;
    padding: 0.65rem 0.8rem;
  }}
  .axis-card .name {{ font-size: 0.78rem; color: #64748b; font-weight: 700; text-transform: uppercase; letter-spacing: 0.03em; }}
  .axis-card .val {{ font-size: 0.95rem; font-weight: 700; color: #059669; margin-top: 0.15rem; }}
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
  iframe.preview {{
    width: 100%;
    border: none;
    display: block;
    background: #F4F6FB;
  }}
  iframe.preview.score {{ height: 1620px; }}
  iframe.preview.special {{ height: 2020px; }}

  .note-line {{
    font-size: 0.82rem;
    color: #64748b;
    margin-top: 0.5rem;
    padding-top: 0.5rem;
    border-top: 1px dashed #cbd5e1;
  }}

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
    <h1>2026-08-01 (토) · 청약 페어 배포 판단</h1>
    <div class="meta">기획전략실 · 사마의 · 산출 2건 · 배포 준비 완료</div>
  </header>

  <div class="verdict">
    <strong>결론</strong>: 오늘 사이클 산출 2건 모두 클레버 4축 검수 통과 · <strong>배포 준비 완료</strong>. 조정 필요 0건. 대표 배포 판단 요청.
  </div>

  <section>
    <h2>① 오늘 사이클 산출 (2건)</h2>
    <table class="util-list">
      <thead>
        <tr><th>#</th><th>유틸</th><th>슬러그</th><th>상태</th><th>조정</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>1</td>
          <td>아파트 청약 가점 계산기<br><span style="font-size:0.78rem;color:#64748b">무주택 기간·부양가족·저축 → 84점 만점</span></td>
          <td><code>apartment-subscription-score</code></td>
          <td class="status">✓ 배포 준비</td>
          <td>—</td>
        </tr>
        <tr>
          <td>2</td>
          <td>아파트 청약 특별공급 자격 판단기<br><span style="font-size:0.78rem;color:#64748b">신혼·다자녀·생애최초·노부모 4유형 탭</span></td>
          <td><code>apartment-subscription-special</code></td>
          <td class="status">✓ 배포 준비</td>
          <td>—</td>
        </tr>
      </tbody>
    </table>
    <p class="note-line">
      벤 판정 근거: 청약 페어(3사이클 연속 최우선 명시 이행) · 부동산 카테고리 축 심화 (매매 → 청약) · High + Mid~High 검색량 = AdSense 신청 임박 상시 트래픽 확보 최적.
    </p>
  </section>

  <section>
    <h2>② 클레버 4축 검수 요약</h2>
    <div class="axis-grid">
      <div class="axis-card">
        <div class="name">정확성</div>
        <div class="val">통과 (수정 1건)</div>
        <div class="note">특별공급 탭 hover invisible text 버그 발견 · 클레버 직접 수정 (<code>button:hover</code> 배경 상속 → <code>.tab-btn:hover</code> <code>var(--primary-soft)</code> 명시).</div>
      </div>
      <div class="axis-card">
        <div class="name">완성도</div>
        <div class="val">통과</div>
        <div class="note">브랜드 승계(코발트 블루 팔레트) · Pretendard · hero-line · 토큰화 완료. 다빈치 접근성 9건 직접 반영.</div>
      </div>
      <div class="axis-card">
        <div class="name">원칙</div>
        <div class="val">통과</div>
        <div class="note">SEO(title·description·OG·twitter·canonical) · JSON-LD WebApplication · <code>&lt;label for&gt;</code> · WCAG AA 5.3~6.7:1 · <code>#ad-slot</code> 위치·<code>min-height:60px</code>.</div>
      </div>
      <div class="axis-card">
        <div class="name">배포준비</div>
        <div class="val">준비 완료</div>
        <div class="note">canonical/og:url/JSON-LD 모두 <code>utils.minon.kr/…</code> 최종 URL · 모바일 <code>viewport</code>·<code>max-width:480px</code> 정합 · 외부 의존 Pretendard CDN 1건.</div>
      </div>
    </div>
  </section>

  <section>
    <h2>③ 사이클 이슈</h2>
    <ul>
      <li><strong>정확성 축 수정 1건 이미 반영</strong> — 특별공급 탭 hover invisible text (버튼 배경 CSS 상속 버그) · 클레버 검수 단계에서 발견·즉시 수정 완료. 재검수 불요.</li>
      <li><strong>토요일 배포 여부</strong> — CLAUDE.md 3절 사이클 원칙은 월·수·금. 오늘 8/1 토요일이나 산출 완성 · 배포 판단은 대표. 오늘 배포 vs 8/3 월 배포 판단 필요.</li>
      <li><strong>반려동물 나이 페어 (7/31 확정 스펙) 개발 착수 대기</strong> — 커밋 <code>9f16bf0</code> · 마이클·클레버 릴레이 미개시. 오늘 청약 페어 배포 판단 병행 대표 지시 필요.</li>
    </ul>
  </section>

  <div class="decision">
    <h2>④ 대표 결정 요청</h2>
    <ul>
      <li><strong>배포 개시</strong> — 청약 페어 2건 · git add + commit + push (Cloudflare Pages 자동 배포) 승인 요청. <code>utils.minon.kr/apartment-subscription-score/</code> · <code>utils.minon.kr/apartment-subscription-special/</code></li>
      <li><strong>배포 시점</strong> — (a) 오늘 8/1 토 즉시 vs (b) 8/3 월 정식 사이클 · 사마의 추천: 배포 준비 완료이므로 <strong>즉시 (a)</strong>. 이미 상시 트래픽 유입 시작 가능.</li>
      <li><strong>반려동물 나이 페어 릴레이</strong> — 스펙 커밋 <code>9f16bf0</code> 기반 마이클·클레버 개발 착수 병행 승인. 배포는 8/3 월 사이클 원칙 유지.</li>
      <li><strong>index.html 랜딩 갱신</strong> — 배포 시 랜딩 목록에 청약 2건 추가 (기존 6건 → 8건).</li>
    </ul>
  </div>

  <section>
    <h2>⑤ 유틸 실물 인라인 확인</h2>
    <p style="font-size:0.85rem;color:#64748b">아래 iframe으로 실물 UI·계산 동작 즉시 확인 가능. 배포 전 최종 손검증용.</p>

    <div class="preview-block">
      <div class="head">
        <span>1. 청약 가점 계산기</span>
        <span class="slug">/apartment-subscription-score/</span>
      </div>
      <iframe class="preview score" srcdoc="{score}" title="청약 가점 계산기"></iframe>
    </div>

    <div class="preview-block">
      <div class="head">
        <span>2. 청약 특별공급 자격 판단기</span>
        <span class="slug">/apartment-subscription-special/</span>
      </div>
      <iframe class="preview special" srcdoc="{special}" title="청약 특별공급 자격 판단기"></iframe>
    </div>
  </section>

  <section>
    <h2>⑥ 산출 파일 경로</h2>
    <ul>
      <li><code class="path">2026-08-01/apartment-subscription-score/index.html</code> (19,580 bytes)</li>
      <li><code class="path">2026-08-01/apartment-subscription-special/index.html</code> (27,941 bytes)</li>
      <li><code class="path">2026-08-01/00-유틸후보.md</code> · <code class="path">2026-08-01/design-notes.md</code></li>
    </ul>
  </section>

</main>
</body>
</html>
"""

archive_path = BASE / "04-보고서.html"
archive_path.write_text(REPORT, encoding="utf-8")

OUTBOX.mkdir(exist_ok=True)
outbox_path = OUTBOX / "webutils_보고서_2026-08-01.html"
shutil.copyfile(archive_path, outbox_path)

print(f"archive: {archive_path} ({archive_path.stat().st_size:,} bytes)")
print(f"outbox:  {outbox_path} ({outbox_path.stat().st_size:,} bytes)")
