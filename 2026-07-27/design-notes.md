# 2026-07-27 디자인 세션 · 웹유틸 2건 · 부동산

## 현재 상태
- 단계: 피카소 시안
- 다음: 피카소
- 반려 지목: —
- 왕복 회차: 1/5

## 브랜드 승계
- 이전 사이클 참조: `2026-07-24/` (wedding-gift-calculator · funeral-condolence-calculator)
- 승계 · 조정 내역: 
  - 기조: **"조용한 신뢰"** (사용자는 빠른 답 원함 · 화려함 × · 정보 중심)
  - 타이포: Pretendard (Google Fonts CDN · display=swap)
  - 시각 위계: h1 1.5rem · 폼레이블 0.9rem · 결과금액 2.25rem · 서브 0.85rem 등 고정
  - 색 팔레트: 유틸별 분기 (지난번: 따뜻함/쿨 톤 구분)
  - 이번 추가 고려: 부동산 · 법적/재무 도메인 → **신뢰감 · 안정성** 강조 필요

---

## 인풋 (마이클)
- `acquisition-tax-calculator/index.html` — 취득세 계산기
- `real-estate-commission-calculator/index.html` — 부동산 중개 수수료 계산기

---

## 아웃풋 (대기)
다빈치가 부동산 도메인용 색 팔레트 2안 정의 후, 피카소가 시안 제시.

---

## 다빈치 · 브랜드 방향 (부동산 사이클)

### 승계 원칙
- "조용한 신뢰" 기조 · Pretendard · 시각 위계 수치 전부 승계
- CDN: jsDelivr (`cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard-dynamic-subset.css`) — Google Fonts 아님
- `@keyframes resultReveal` + `display:none` 방식 — 지난 달리 수정 사항 그대로 유지
- 히어로 라인: 이번엔 두 유틸 모두 추가 (부동산 = 결정의 무게 → 라인으로 시각적 착지)

### 도메인 톤
부동산·세금·법정 수수료 — 사용자는 수억원 결정 앞에서 열어봄. 색이 흔들리면 안 됨.
**땅의 안정감** → 그린 계열과 티얼 계열을 선택.
지난 사이클에서 `#2D4A6B` 네이비를 장례식에 썼으므로, 블루 계열은 미세하게 다른 영역(티얼)으로 이동.

### 색 팔레트 분기

#### 취득세 계산기 (acquisition-tax-calculator) — 포레스트 그린
세금 납부 = 공적 의무 · 묵직함 · 국가 신뢰 → 포레스트 그린
| 토큰 | 값 | 용도 |
|---|---|---|
| `--bg` | `#F6F8F5` | 배경 (그린 언더톤 오프화이트) |
| `--primary` | `#2C5F3E` | 버튼·accent·결과금액·라인 데코 |
| `--primary-hover` | `#1E4B2E` | 버튼 hover |
| `--card-bg` | `#E8F0E9` | 결과 카드 배경 |
| `--card-border` | `#BDD4BF` | 결과 카드 border |
| `--text` | `#111C17` | 본문 (그린 언더톤 블랙) |
| `--text-sub` | `#5A7060` | 서브텍스트 · .label-note · .rate-badge · .disclaimer |
| `--border` | `#B8CCB9` | 폼 요소 border |
| `--focus` | `#2C5F3E` | focus outline |
| `--error` | `#B83A28` | 에러 |
| `--total-line` | `#2C5F3E` | `.result-row.total border-top` |

접근성: `#2C5F3E` vs `#fff` = 약 7.5:1 ✓

히어로 데코: `.hero-line` 있음 (width 2.5rem · height 2px · background var(--primary))

#### 중개수수료 계산기 (real-estate-commission-calculator) — 딥 티얼
중개 = 연결·협상 · 실용적 행동 → 딥 티얼 (청록)
| 토큰 | 값 | 용도 |
|---|---|---|
| `--bg` | `#F5F7FA` | 배경 (블루-쿨 오프화이트) |
| `--primary` | `#1C6070` | 버튼·accent·결과금액·라인 데코 |
| `--primary-hover` | `#124A58` | 버튼 hover |
| `--card-bg` | `#E6F2F5` | 결과 카드 배경 |
| `--card-border` | `#B0D0DA` | 결과 카드 border |
| `--text` | `#0F1E22` | 본문 |
| `--text-sub` | `#527580` | 서브텍스트 · .label-note · .rate-badge · .disclaimer |
| `--border` | `#B0C8D0` | 폼 요소 border |
| `--focus` | `#1C6070` | focus outline |
| `--error` | `#B83A28` | 에러 |
| `--total-line` | `#1C6070` | `.result-row.total border-top` |

접근성: `#1C6070` vs `#fff` = 약 7.1:1 ✓

히어로 데코: `.hero-line` 있음

---

## 피카소 구현 지시 (왕복 1회차)

**공통 (두 파일 모두)**
1. Pretendard CDN: `<link rel="preconnect" href="https://cdn.jsdelivr.net">` + `<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard-dynamic-subset.css">`
2. CSS custom properties: `:root { --bg: ...; ... }` — 파일별 팔레트 각각 선언
3. body/h1/레이블/버튼: `font-family: 'Pretendard', -apple-system, ...` 적용
4. h1 font-size: 1.5rem (기존 1.4rem → 스펙 정합)
5. `.hero-line` 추가: h1 바로 아래, `width:2.5rem; height:2px; background:var(--primary); margin:0.5rem 0 1.5rem;`
   → HTML에 `<div class="hero-line"></div>` 삽입 (h1과 .subtitle 사이)
6. `@keyframes resultReveal` + `display:none` 방식:
   ```css
   @keyframes resultReveal {
     from { opacity: 0; transform: translateY(6px); }
     to   { opacity: 1; transform: translateY(0); }
   }
   #result { display: none; ... }
   #result.show { display: block; animation: resultReveal 200ms ease-out both; }
   ```
7. 버튼: border-radius 10px · `transition: transform 150ms ease, box-shadow 150ms ease` · hover `translateY(-1px) + box-shadow 0 4px 12px rgba(0,0,0,0.15)` · active `translateY(0) + shadow none`
8. 결과 카드: `background: var(--card-bg); border: 1px solid var(--card-border); border-radius: 12px;`
9. `.result-row.total { border-top: 2px solid var(--primary); }` (기존 하드코딩 `#222` → var)
10. `.rate-badge { color: var(--text-sub); }` (기존 `#666` → var)
11. `.disclaimer { color: var(--text-sub); }` (기존 `#888` → var)
12. `.label-note { color: var(--text-sub); }` (기존 `#666` → var)
13. `input[type="number"]`: `border: 1px solid var(--border); focus: outline: 2px solid var(--focus);`
14. `accent-color: var(--primary)` — radio/checkbox
15. 폼 select/input border → `var(--border)`, focus → `var(--focus)`

**중개수수료 전용** (select 있음)
16. select: `appearance:none;` + SVG chevron (`stroke='%231C6070'` — 티얼 hex 인코딩)
    ```
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath fill='none' stroke='%231C6070' stroke-width='2' d='M4 6l4 4 4-4'/%3E%3C/svg%3E");
    background-repeat: no-repeat; background-position: right 0.75rem center; background-size: 1rem; padding-right: 2.5rem;
    ```

**취득세 전용** (select 없음 — 이미 없음, 추가 불필요)

**유지 대상 (절대 손대지 않음)**
- 모든 `<meta>` SEO 태그 · JSON-LD `<script>`
- `<div id="ad-slot">`
- JS `<script>` 전체 (계산 로직)
- `.hidden` 클래스 (중개수수료 JS 동적 show/hide 의존)

완료 후 이 파일에 "피카소 시안 결과" 섹션에 16개 항목 ✓/✗ + 확신 못 한 부분 기록.

---

## 피카소 시안 결과
(대기)

---

## 달리 검토
(대기)

---

## 다빈치 최종 판정
(대기)
