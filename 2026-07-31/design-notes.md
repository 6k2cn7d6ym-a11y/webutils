# 2026-07-31 디자인 세션 · 웹유틸 2건 · 날씨·공휴일

## 현재 상태
- 단계: 피카소 실행 (다빈치 승인 · 달리 이관 + 다빈치 보완 1건)
- 다음: 피카소
- 반려 지목: —
- 왕복 회차: 1/5

## 브랜드 승계
- 이전 사이클 참조: `2026-07-29/` (wbgt-heat-work-calculator · golden-vacation-planner-2026)
- 승계 · 조정 내역:
  - 기조: "조용한 신뢰" 유지
  - 타이포: Pretendard (jsDelivr CDN) 유지
  - 시각 위계 수치 유지
  - `@keyframes resultReveal` + `display:none` 방식 — 체감온도에만 적용 (`.result.visible`)
  - 공휴일대체: JS 없음 → 애니메이션 불필요
  - CDN: `cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard-dynamic-subset.css`

---

## 인풋 (마이클)
- `apparent-temperature-calculator/index.html` — 체감온도 계산기
- `public-holiday-substitute-2026/index.html` — 2026 광복절 대체공휴일 안내

---

## 다빈치 · 브랜드 방향

### 구조 분석 (피카소 작업 전 필독)

**체감온도 구조:**
- `.card` 기반 레이아웃 + body `background: #f4f4f4` → `var(--bg)` 교체
- 마이클 `#0ea5e9` (스카이 블루) — 날씨 도메인 의도적 선택, 방향 유지하되 접근성 보강
- 결과: `.result.visible` (`.show` 아님) → `@keyframes resultReveal` 방식 적용
- **절대 유지**: `.lvl-fine/caution/warning/danger`, `.lvl-cold-fine/caution/warning/danger/extreme`, `.lvl-neutral` 9종 (안전·날씨 신호색)
- `.formula-badge { background:#f0f9ff; color:#0369a1; border:1px solid #bae6fd; }` → `var(--primary-soft)` 계열로 교체 가능

**공휴일대체 구조:**
- JS 없음 — 순수 정적 HTML. 결과 애니메이션 불필요.
- 마이클 `#1d4ed8` (코발트 블루) — 공적·제도 도메인. 이미 대비 6.6:1 ✓. 방향 유지.
- CSS만 변경 (JS class 토글 없음):
  - `.fact-box`, `.fact-date`, `.fact-confirm`, `.hdate`, `.highlight-row`, `.cal-cell.subst`, `.rule-bullet` 모두 CSS → 변경 가능
  - `.cal-cell.holiday` (빨강) · `.cal-cell.weekend` (빨강 텍스트) · `.cal-cell.leave` (노랑) · `.cal-cell.dimmed` (회색) → **유지 필수** (달력 기능 색)

### 색 팔레트 분기

#### 체감온도 계산기 — 하늘 청 (날씨·기후·체감)
마이클 `#0ea5e9` 유지 + 접근성 보강 (기존 = 2.7:1 → 더 깊게)

| 토큰 | 값 | 용도 |
|---|---|---|
| `--bg` | `#F3F7FA` | 배경 (하늘빛 오프화이트) |
| `--primary` | `#0072A8` | 버튼·focus·disclaimer border (대비 약 5.0:1 ✓) |
| `--primary-hover` | `#005A86` | 버튼 hover |
| `--primary-soft` | `#E0F2FB` | .formula-badge 배경 |
| `--primary-soft-border` | `#BAE3F7` | .formula-badge border |
| `--primary-soft-text` | `#00567E` | .formula-badge 텍스트 |
| `--text` | `#111B24` | 본문 |
| `--text-sub` | `#52697A` | .subtitle · .field-note · .formula-info |
| `--border` | `#BDD0DA` | 폼 요소 border |
| `--focus` | `#0072A8` | focus outline |
| `--error` | `#B83A28` | 에러 |

히어로 데코: `.hero-line` 추가 (2.5rem × 2px · `var(--primary)`)
disclaimer border: `var(--primary)` — 날씨·안전 도메인, 경각심 앵커 역할 (WBGT 패턴 동일)

#### 공휴일대체 계산기 — 코발트 블루 (공적·제도·법령)
마이클 `#1d4ed8` 그대로 primary로 정의 + CSS var 체계화

| 토큰 | 값 | 용도 |
|---|---|---|
| `--bg` | `#F4F6FB` | 배경 (쿨한 블루 언더톤 오프화이트) |
| `--primary` | `#1D4ED8` | fact-date·fact-confirm·hdate·subst·highlight (대비 6.6:1 ✓) |
| `--primary-soft` | `#EFF6FF` | fact-box bg·highlight-row bg |
| `--primary-soft-border` | `#BFDBFE` | fact-box border |
| `--text` | `#0F1624` | 본문 |
| `--text-sub` | `#5A6680` | .subtitle · .fact-sublabel · .hreason |
| `--border` | `#D0D8E8` | 표 border · .holiday-list border-bottom |
| `--error` | `#B83A28` | 에러 (미사용이지만 선언) |

히어로 데코: `.hero-line` 추가 (2.5rem × 2px · `var(--primary)`)
disclaimer border: `var(--border)` — 법률 참조 문구, 안전 경고 아님 → 중립 처리

---

## 피카소 구현 지시 (왕복 1회차)

### 공통 (두 파일)
1. Pretendard CDN:
   ```html
   <link rel="preconnect" href="https://cdn.jsdelivr.net">
   <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard-dynamic-subset.css">
   ```
2. `font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, 'Malgun Gothic', sans-serif` — body
3. CSS custom properties `:root { ... }` 선언
4. h1: 1.4rem → 1.5rem · Pretendard 700
5. `.subtitle` color → `var(--text-sub)`
6. body `background: #f4f4f4` → `var(--bg)`
7. `.hero-line` 추가 (h1과 `.subtitle` 사이):
   HTML: `<div class="hero-line"></div>`
   CSS: `width:2.5rem; height:2px; background:var(--primary); margin:0.35rem 0 0.45rem; border-radius:2px;`

### 체감온도 전용
8. `:root` 팔레트 → 하늘 청 토큰 선언
9. 버튼: `background: var(--primary)` · hover `var(--primary-hover)` · border-radius 8px → 10px · `transition: transform 150ms ease, box-shadow 150ms ease` · hover `translateY(-1px) + box-shadow 0 4px 12px rgba(0,0,0,0.15)` · active `translateY(0)`
10. `input[type="number"]:focus` → `border-color: var(--focus); outline: none;`
11. `button:focus-visible` → `outline: 3px solid var(--focus); outline-offset: 2px;`
12. 결과 카드 등장 (`visible` 클래스 기준):
    ```css
    @keyframes resultReveal {
      from { opacity: 0; transform: translateY(6px); }
      to   { opacity: 1; transform: translateY(0); }
    }
    .result { display: none; }
    .result.visible { display: block; animation: resultReveal 200ms ease-out both; }
    ```
13. `.formula-badge` → `background: var(--primary-soft); color: var(--primary-soft-text); border: 1px solid var(--primary-soft-border);`
14. `.field-note` → `color: var(--text-sub)`
15. `.formula-info` → `color: var(--text-sub)` (기존 `#777`)
16. `.disclaimer` → `color: var(--text-sub); border-left-color: var(--primary);`
17. **절대 유지**: `.lvl-fine/caution/warning/danger`, `.lvl-cold-fine/caution/warning/danger/extreme`, `.lvl-neutral` 9종 색 변경 금지
18. SEO 태그·JSON-LD·`#ad-slot`·JS `<script>` 전체 유지

### 공휴일대체 전용
19. `:root` 팔레트 → 코발트 블루 토큰 선언
20. `.fact-box` → `background: var(--primary-soft); border: 2px solid var(--primary-soft-border);`
21. `.fact-date` → `color: var(--primary)`
22. `.fact-confirm` → `background: var(--primary); color: #fff;`
23. `.cal-cell.subst` → `background: var(--primary-soft); color: var(--primary);`
24. `.highlight-row td` → `background: var(--primary-soft); color: var(--primary);`
25. `.hdate` → `color: var(--primary)`
26. `.rule-bullet` → `background: var(--primary-soft-border);` (기존 `#60a5fa` → 코발트 계열 통일)
27. `.leave-table th` → `background: #F0F2F8; font-weight: 600;` (기존 `#f0f0f0` → 블루 언더톤으로 미세 조정)
28. `.disclaimer` → `color: var(--text-sub); border-left-color: var(--border);` (법률 참조 → 중립 색)
29. `.holiday-list li` border-bottom → `border-bottom: 1px solid var(--border);`
30. `p style="color:#aaa"` 인라인 스타일 두 곳 → CSS class `.footnote { font-size:0.78rem; color:var(--text-sub); margin-top:0.4rem; }` 로 교체하고 HTML도 교체
31. JS 없음 → 애니메이션 불필요
32. **유지**: `.cal-cell.holiday` (빨강) · `.cal-cell.weekend` (빨강 텍스트) · `.cal-cell.leave` (노랑) · `.cal-cell.dimmed` 유지 — 달력 기능 색

### 다빈치 보완 (시각 강도 보존 · 왕복 1회차)
33. **`.rule-bullet background`** — 지시 26번의 `var(--primary-soft-border)`(`#BFDBFE` 파스텔) 대신 **`var(--primary)`(`#1D4ED8`) 사용**. 마이클 원본 `#60a5fa`는 규칙 마커의 시각 강조 요소 · 파스텔로 교체 시 배경 대비 옅어져 강조 기능 상실. Primary로 톤 통일하면서 시각 강도 보존 (자식 텍스트가 있으면 흰색 대비 6.6:1).

### 다음 사이클 학습 자산
- **3단 소프트 토큰 패턴** 채택 확정: `--primary-soft`(bg) · `--primary-soft-border`(border) · `--primary-soft-text`(text). formula-badge·fact-box 등 강조 배지/박스 요소에 표준. 지난 사이클 두 번째 이후 나온 새 패턴.
- **rule-bullet류 마커 원칙**: 배경 채우는 마커/불릿은 `var(--primary)` 사용(파스텔 아님). 파스텔은 넓은 면적 배경(box/badge)에만 · 좁은 강조 요소에는 강도 유지.

완료 후 이 파일 "피카소 시안 결과" 섹션에 33개 항목 ✓/✗ + 확신 못 한 부분 기록.

---

## 피카소 시안 결과
(대기)

---

## 달리 검토
(대기)

---

## 다빈치 최종 판정
(대기)
