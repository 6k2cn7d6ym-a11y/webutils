# 2026-07-29 디자인 세션 · 웹유틸 2건 · 라이프스타일·안전

## 현재 상태
- 단계: 피카소 실행 (다빈치 승인 · 달리 이관 + 다빈치 보완 1건)
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

### 다빈치 보완 (도메인 신호 강도 · 왕복 1회차)
26. **WBGT `.disclaimer border-left-color`** — 지시 15번의 `var(--border)`(`#D0C8C0`) 대신 **`var(--primary)`(`#C84A00`) 사용**. 폭염·산업안전 도메인에서 disclaimer는 tone-mute가 아니라 경각심 신호 앵커 · 크림 배경에 옅은 회색 border는 신호로 안 읽힘. 황금연차 지시 23번은 여행 도메인 톤 유지 → 원안 `var(--border)` 그대로.

### 다음 사이클 학습 자산
- 지난 사이클 다빈치 보완 ③ (`.result-main color: var(--primary)`)은 **안전·위험 신호 색 시스템(`.lvl-*`)이 결과 시각화를 담당하는 도메인에서는 적용 안 함**. 브랜드 primary는 프레임(버튼·hero-line·disclaimer border)에만, 결과 시각화는 도메인 색 시스템에 위임.

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

---

## 클레버 검수 (2026-07-29 04:xx · 개발팀 팀장 단독 방)

### 4축 검수 결과
- **정확성**: 수정 (크리스마스 요일 오타 2건 · 아래 수정 항목 참조)
- **완성도**: 수정 (디자인팀 피카소 시안 **미반영** — 두 파일 모두 마이클 초안 그대로 · design-notes 25개 지시 항목 반영 0)
- **원칙**: OK (SEO 태그·JSON-LD·접근성 aria·광고 슬롯·JS 문법 전부 통과 · 두 파일 `node --check` PASS)
- **배포준비**: **배포 불가** — 디자인팀 반영 없이는 이전 사이클 브랜드 승계 파탄 · 대비비 미달(#e45c00 = 3.5:1 < WCAG AA)

### 수정 항목 (클레버 직접 수정)

**golden-vacation-planner-2026/index.html · 크리스마스 시나리오 요일 오타 정정**
- 시나리오 2 period: `12/24(수)` → `12/24(목)` · 실제 2026-12-24 = 목 (Python date 검증)
- 시나리오 3 period: `12/22(월)` → `12/22(화)` · 실제 2026-12-22 = 화
- 이유: 요일 표기가 실제 캘린더와 어긋나면 사용자 신뢰 즉시 파탄. 배포 전 반드시 잡아야 하는 수치 오류라 클레버 직접 수정. 인라인 주석에 `[클레버 수정: 요일 오타 정정 · 실제 캘린더 대조]` 명시.

**추가 검증 완료 (오류 없음)**:
- 광복절·추석·개천절+한글날 시나리오 요일·일수 전부 실제 캘린더와 일치
- WBGT 계산: Stull 2011 습구온도 근사식 · 안전보건공단 25/28/31 단계별 분기 정확
- WBGT LEVELS 배열 순증 정렬 + `wbgt < max` for-loop → 경계 처리 정확 (25.0 = 정상, 28.0 = 주의)

### 수정 안 하고 남긴 이슈 (팀장 판단 필요 · 이월)

1. **황금연차 title/subtitle의 "여름" 프레이밍 vs 실제 커버리지 불일치**
   - title: `2026 여름 황금연차 계산기` · subtitle: `광복절·추석·한글날·크리스마스`
   - 실제 EVENTS: 광복절(8월) · 추석(9월) · 개천절+한글날(10월) · 크리스마스(12월) → 여름 아님
   - 00-유틸후보.md 채택 근거는 "8월 시류(광복절 임박)" 여름 프레이밍 · 마이클이 재사용성 확보 차원 확장
   - 판정: **마케팅팀 결정 안건** (SEO 키워드 vs 카피 정합) · 클레버 판단 영역 밖 · 사마의 일일보고에서 마케팅팀 상신 요망
   - subtitle에도 개천절 빠져 있음 (있는 이벤트인데 subtitle 4개 나열에서 누락)

2. **디자인팀 피카소 시안 전면 미반영 (25개 지시 항목 반영 0)**
   - `design-notes.md § 피카소 시안 결과` = "(대기)" 상태
   - 미반영 항목 (전부): Pretendard CDN · CSS custom properties · body bg · hero-line · @keyframes resultReveal · 버튼 hover transform · 색 팔레트 (WBGT 딥버밀리온 · 황금연차 오션블루) · disclaimer border-left 다빈치 보완
   - 특히 대비비 이슈: 마이클 원본 `#e45c00` 오렌지 on white ≈ 3.5:1 (WCAG AA 4.5:1 미달) → 디자인팀 `#C84A00` 조정본 필수 반영
   - 클레버가 디자인 지시를 직접 코드에 붙이는 건 왕복 사이클(피카소→달리→다빈치) 무력화 · 명의 사칭 소지 → 반영 안 함
   - **필수 액션**: 피카소 실행 → 달리 검토 → 다빈치 최종 판정 → 클레버 재검수 후 배포 판정

3. **파일 위치 (검수 결과와 무관 · 관행 확인용)**
   - 현재: `2026-07-29/{slug}/index.html` (자율 세션 산출물 폴더)
   - 배포 시: 루트 `{slug}/index.html`로 이동 필요 (CLAUDE.md § 6·7)
   - 배포 실행 = 대표 직접 지시 별도 (클레버 검수 방 스코프 밖 · `_COMMON.md § 7` 준수)

### 배포 준비 상태

**배포 불가 · 사유: 디자인팀 피카소 시안 미반영 · 브랜드 승계 파탄 + 대비비 WCAG AA 미달**

배포 조건 (재검수 필요):
1. 피카소 → 달리 → 다빈치 왕복 완료 (design-notes.md 각 섹션 채워짐)
2. 25개 지시 항목 반영 확인
3. 클레버 재검수 (기능·완성도·원칙·배포준비 4축 전면 재판정)
4. 사마의 일일보고 → 대표 직접 지시로 파일 이동·git push 실행

**클레버 검수 완료 · 재검수 대기 상태**

