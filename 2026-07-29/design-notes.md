# 2026-07-29 디자인 세션 · 웹유틸 2건 · 라이프스타일·안전

## 현재 상태
- 단계: 피카소 시안
- 다음: 피카소
- 반려 지목: —
- 왕복 회차: 1/5

## 브랜드 승계
- 이전 사이클 참조: `2026-07-27/` (acquisition-tax-calculator · real-estate-commission-calculator)
- 승계 · 조정 내역:
  - 기조: "조용한 신뢰" 유지
  - 타이포: Pretendard (jsDelivr CDN) 유지
  - 시각 위계 수치 유지
  - `@keyframes resultReveal` + `display:none` 방식 (WBGT에 적용 · 황금연차는 불필요)
  - CDN: `cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard-dynamic-subset.css`

---

## 인풋 (마이클)
- `wbgt-heat-work-calculator/index.html` — 폭염 WBGT 계산기
- `golden-vacation-planner-2026/index.html` — 2026 황금연차 계산기

---

## 다빈치 · 브랜드 방향

### 구조 분석 (피카소 작업 전 필독)

**WBGT 계산기 구조:**
- `.card` 클래스 기반 레이아웃 (`.form-group` 아님)
- body background: `#f4f4f4` (회색) → `var(--bg)`로 교체
- 결과: `.result.visible` 클래스 토글 (`.show` 아님!) → `display:none` + `@keyframes resultReveal` 적용 시 `.result.visible` 기준으로
- 마이클이 이미 `#e45c00` 오렌지 선택 — 폭염·안전 도메인 의도적 선택, 방향 유지
- **절대 금지**: `.lvl-safe/caution/warning/danger` 색 변경 금지 (안전 신호 색, 기능 의존)
- `input[type="number"]` + `select` focus: `border-color: #e45c00` → `var(--focus)`로 통일

**황금연차 계산기 구조:**
- 결과 카드 없음 — 초기 로드부터 이벤트 카드 전부 표시 (JS renderEvents 호출) → `@keyframes resultReveal` 불필요
- 아래 CSS들은 모두 CSS 파일 내에 있어 변경 가능 (JS는 class만 토글):
  - `.days-badge.best { background: #2563eb; }` → `var(--primary)` 교체 가능
  - `.scenario-row.highlight { background: #eff6ff; }` → `var(--highlight-bg)` 교체 가능
  - `input[type="number"]:focus { border-color: #2563eb; }` → `var(--focus)` 교체 가능
  - `.lb-low { color: #1d4ed8; border: 1px solid #bfdbfe; }` → 연차 뱃지색 → **변경 금지** (기능 색상 신호)
- `.event-card border: 2px solid #e5e5e5` → `var(--border)` 교체 가능
- body background: `#f4f4f4` → `var(--bg)`

### 색 팔레트 분기

#### WBGT 계산기 — 딥 버밀리온 (폭염·경각심·안전)
마이클 오렌지 존중 + 접근성 보강 (기존 `#e45c00` = 3.5:1 → 더 깊게)

| 토큰 | 값 | 용도 |
|---|---|---|
| `--bg` | `#F6F4F1` | 배경 (따뜻한 크림오프화이트) |
| `--primary` | `#C84A00` | 버튼 · focus · accent (대비 약 4.7:1 ✓) |
| `--primary-hover` | `#A33C00` | 버튼 hover |
| `--text` | `#1A1410` | 본문 |
| `--text-sub` | `#6B5E55` | 서브텍스트 · note · unit |
| `--border` | `#D0C8C0` | 폼 요소 border |
| `--focus` | `#C84A00` | focus outline |
| `--error` | `#B83A28` | 에러 |

히어로 데코: `.hero-line` 추가 (2.5rem × 2px · `var(--primary)`)
`.disclaimer border-left: 3px solid #e0e0e0` → `var(--border)` 교체

#### 황금연차 계산기 — 오션 블루 (여름·휴가·설렘)
여름 하늘과 바다. 기존 Michael 블루(`#2563eb`) 계열 유지하되 깊게 조정.

| 토큰 | 값 | 용도 |
|---|---|---|
| `--bg` | `#F2F6FA` | 배경 (청명한 하늘빛 오프화이트) |
| `--primary` | `#1568A0` | 버튼 · focus · best badge (대비 약 5.7:1 ✓) |
| `--primary-hover` | `#0D5282` | 버튼 hover |
| `--highlight-bg` | `#E6F0F8` | `.scenario-row.highlight` 배경 |
| `--text` | `#0F1E2A` | 본문 |
| `--text-sub` | `#52677A` | 서브텍스트 · hint |
| `--border` | `#BDD0DF` | 폼 요소 border · `.event-card` border |
| `--focus` | `#1568A0` | focus outline |
| `--error` | `#B83A28` | 에러 |

히어로 데코: `.hero-line` 추가 (2.5rem × 2px · `var(--primary)`)

---

## 피카소 구현 지시 (왕복 1회차)

### 공통 (두 파일)
1. Pretendard CDN:
   ```html
   <link rel="preconnect" href="https://cdn.jsdelivr.net">
   <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard-dynamic-subset.css">
   ```
2. `font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, 'Malgun Gothic', sans-serif` — body에 적용
3. CSS custom properties `:root { --bg: ...; ... }` 선언
4. h1 font-size: 1.4rem → 1.5rem · Pretendard 700
5. `.subtitle` color → `var(--text-sub)`
6. label color: `#333` → `var(--text)` 또는 그냥 inherit
7. 버튼: `background: var(--primary)` · hover `var(--primary-hover)` · border-radius 8px (현재 7px, 작은 변경) · `transition: transform 150ms ease, box-shadow 150ms ease` · hover `translateY(-1px) + box-shadow 0 4px 12px rgba(0,0,0,0.15)` · active `translateY(0)`
8. body `background: #f4f4f4` → `var(--bg)`
9. `.hero-line` 추가: h1과 `.subtitle` 사이에 `<div class="hero-line"></div>` 삽입, CSS: `width:2.5rem; height:2px; background:var(--primary); margin:0.35rem 0 0.45rem; border-radius:2px;`

### WBGT 전용
10. `:root` 팔레트 → 딥 버밀리온 토큰 선언
11. `input[type="number"]:focus, select:focus` → `border-color: var(--focus)` (기존 `#e45c00`)
12. `button:focus-visible` → `outline: 3px solid var(--focus)`
13. 결과 카드 등장 애니메이션:
    ```css
    @keyframes resultReveal {
      from { opacity: 0; transform: translateY(6px); }
      to   { opacity: 1; transform: translateY(0); }
    }
    .result { display: none; }
    .result.visible { display: block; animation: resultReveal 200ms ease-out both; }
    ```
    (기존 `.result { display:none }` + `.result.visible { display:block }` 구조 유지 · 클래스명 `visible` 그대로)
14. `.note` color → `var(--text-sub)`
15. `.disclaimer` color → `var(--text-sub)` · `border-left-color: var(--border)`
16. **절대 금지**: `.lvl-safe/caution/warning/danger`, `.r-safe/caution/warning/danger` 색 변경 금지

### 황금연차 전용
17. `:root` 팔레트 → 오션 블루 토큰 선언
18. `input[type="number"]:focus` → `border-color: var(--focus)`
19. `.days-badge.best { background: var(--primary); color: #fff; }` (기존 `#2563eb` → `var(--primary)`)
20. `.scenario-row.highlight { background: var(--highlight-bg); }` (기존 `#eff6ff`)
21. `.event-card { border: 2px solid var(--border); }` (기존 `#e5e5e5`)
22. `.hint` color → `var(--text-sub)`
23. `.disclaimer` color → `var(--text-sub)` · `border-left-color: var(--border)`
24. **변경 금지**: `.lb-zero/lb-low/lb-mid/lb-high` 색 (연차 분류 신호색)
25. `@keyframes resultReveal` 불필요 — 이벤트 카드는 초기 로드부터 표시

### 유지 대상
- 마이클 SEO `<meta>` 전체 · JSON-LD · `#ad-slot` 위치·크기 · JS `<script>` 전체
- WBGT: `.card` 구조 · `.form-row` · `.wbgt-num` · `.level-bar` · `.ref-table`
- 황금연차: `.event-card` · `.scenario-row` · `.leave-badge` · `.legend` 구조

완료 후 이 파일 "피카소 시안 결과" 섹션에 25개 항목 ✓/✗ + 확신 못 한 부분 기록.

---

## 피카소 시안 결과
(대기)

---

## 달리 검토
(대기)

---

## 다빈치 최종 판정
(대기)
