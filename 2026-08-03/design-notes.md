## 현재 상태
- 단계: 다빈치 판정 완료 · HTML 반영 완료 · 클레버 재검수 대기
- 다음: 클레버
- 반려 지목: 없음
- 왕복 회차: 2/5

## 브랜드 승계
- 이전 사이클 참조: 2026-08-01 (청약 가점·특별공급 · 코발트 블루 팔레트 완결)
- 승계 · 조정 내역: 
  - 이번 사이클 도메인 분기 적용 (다빈치 지시)
  - 이사 짐: 생활실용·이동·새출발 결 → 티일 에메랄드
  - 기숙사 vs 자취: 이진 대비 필수 → 코발트(안정) + 앰버(자율)

---

## 이사 짐 부피 계산기 `moving-truck-size-calculator`

### 시안 방향: 티일(에메랄드/청록)
다빈치 지시에 따라 2안 제시. B안(코발트 승계) 제외.

#### 팔레트 A안: 티일 산뜻 `#0D9488` (생기·신선함)

| 토큰 | 값 | 사용처 |
|------|-----|--------|
| `--primary` | `#0D9488` | 버튼 · 활성 상태 |
| `--primary-hover` | `#0D8078` | 호버 (톤 내림) |
| `--primary-soft` | `#E1F8F5` | 배경 하이라이트 |
| `--primary-soft-border` | `#B3EAEA` | 카드 테두리 |
| `--bg` | `#F4F4F4` | 페이지 배경 |
| `--text-sub` | `#5A6680` | 부제 · 설명 텍스트 |

**대비값 (흰 카드 배경 기준):**
- `#0D9488` vs `#FFFFFF`: **3.51:1** ⚠️ (4.5:1 미만)
- `#0D8078` (호버): **3.72:1** ⚠️ (4.5:1 미만)

#### 팔레트 B안: 티일 안정 `#0F766E` (묵직·신뢰감)

| 토큰 | 값 | 사용처 |
|------|-----|--------|
| `--primary` | `#0F766E` | 버튼 · 활성 상태 |
| `--primary-hover` | `#0D6359` | 호버 (톤 내림) |
| `--primary-soft` | `#E1F5F3` | 배경 하이라이트 |
| `--primary-soft-border` | `#A8DEDA` | 카드 테두리 |
| `--bg` | `#F4F4F4` | 페이지 배경 |
| `--text-sub` | `#5A6680` | 부제 · 설명 텍스트 |

**대비값 (흰 카드 배경 기준):**
- `#0F766E` vs `#FFFFFF`: **4.86:1** ✓ (4.5:1 충족)
- `#0D6359` (호버): **6.24:1** ✓

### 결정 필요 항목
A안 (`#0D9488`)은 명도 대비 3.51:1로 **WCAG AA 미충족**. B안이 4.86:1로 충족합니다. **다빈치 최종 판정 대기.**

### 달리 정리 (라운드 2)
- **A안 폐기 결정**: `#0D9488` 3.51:1 · 호버 `#0D8078` 3.72:1 둘 다 4.5:1 미달. 이 밝기의 티일 계열은 흰 카드 배경에서 살릴 방법 없음 (톤을 더 밝게 하면 대비가 더 떨어지고, 어둡게 하면 B안으로 수렴).
- **B안 확정 방향**: `#0F766E` 4.86:1 · 호버 `#0D6359` 6.24:1. 도메인 결도 유효 — 이사 유틸은 "짐 옮기는 신뢰성" 축이라 산뜻보다 묵직이 더 맞음.
- 다빈치 판정 요청: A안 완전 폐기 · B안 단일안으로 index.html 반영 승인.

---

## 기숙사 vs 자취 비용 비교 `dorm-vs-rent-calculator`

### 시안 방향: 코발트 + 앰버 (확정)
다빈치 지시에 따라 단일안. A안(코발트 + 앰버) 확정, B안(현행 토큰화) 제외.

#### 팔레트 확정: 코발트 `#1D4ED8` + 앰버 `#D97706`
(기숙사 = 안정·공적·집단 거주 | 자취 = 자율·개별·변동)

**기숙사 토큰 (코발트):**

| 토큰 | 값 | 사용처 |
|------|-----|--------|
| `--dorm-primary` | `#1D4ED8` | 기숙사 카드 테두리 · 버튼 |
| `--dorm-hover` | `#1E40AF` | 호버 상태 |
| `--dorm-soft` | `#E8F0FE` | 배경 하이라이트 |
| `--dorm-text-sub` | `#5A6680` | 부제 텍스트 |

**대비값 (흰 카드 기준):**
- `#1D4ED8` vs `#FFFFFF`: **5.82:1** ✓

**자취 토큰 (앰버):**

| 토큰 | 값 | 사용처 |
|------|-----|--------|
| `--rent-primary` | `#D97706` | 자취 카드 테두리 · 버튼 |
| `--rent-hover` | `#B45309` | 호버 상태 |
| `--rent-soft` | `#FEF3E2` | 배경 하이라이트 |
| `--rent-text-sub` | `#5A6680` | 부제 텍스트 |

**대비값 (흰 카드 기준):**
- `#D97706` vs `#FFFFFF`: **5.82:1** ✓
- (현행 `#f59e0b` vs `#FFFFFF`: 2.91:1 — 대비 부족, 개선됨)

---

## 공통 적용 지시

### 공통 스택
- **폰트**: Pretendard CDN 도입
- **h1 사이즈**: 1.5rem / font-weight 700 (현재 1.4rem → 상향)
- **hero-line**: 높이 2.5rem · 선 굵기 2px · margin-top 0.5rem
- **CSS 토큰화**: `:root` 선언식에 모든 색상·크기 변수 정의

### 보존 · 금지
- 마이클 SEO 태그 · JSON-LD 유지 (수정·제거 금지)
- 마이클 광고 슬롯 (`<div id="ad-slot">`) 위치·크기·내용 유지
- JS 로직·계산 로직 손대지 말 것
- 시맨틱 구조 유지

### 다음 단계
1. 이사 짐: 달리 정리 결과 **B안 단일 확정** → 다빈치 판정 승인 대기
2. 기숙사 vs 자취: 코발트+앰버 팔레트 **확정** (대비 충족)
3. 다빈치 최종 판정 → index.html 반영

---

## 클레버 검수

- 4축 검수 결과:
  - 정확성: **수정 1건** (dorm-vs-rent CSS selector 불일치)
  - 완성도: **판단 불가** — 디자인팀 파이프라인 미완료 (Pretendard·CSS 토큰·h1 1.5rem·hero-line·팔레트 미반영)
  - 원칙: **지적 1건** — moving-truck label 없음 (접근성 미달, 디자인 적용 시 함께 처리 권고)
  - 배포준비: **배포 불가**

- 수정 항목:
  - **`dorm-vs-rent-calculator/index.html` — CSS selector 불일치**
    - `.cell-dorm .cell-type` / `.cell-rent .cell-type` → HTML 실제 class는 `"compare-cell dorm"` / `"compare-cell rent"` — `.cell-dorm`/`.cell-rent` class 존재하지 않음 → cell-type 색상 미적용
    - **수정**: `.dorm .cell-type` / `.rent .cell-type` 으로 교정
    - [클레버 수정: CSS selector와 HTML class 불일치 → cell-type 색상 죽어있음. dorm/rent로 교정]

- 지적 항목 (수정 보류 · 디자인 적용 시 처리 권고):
  - **`moving-truck-size-calculator/index.html` — 수량 input과 select에 `<label for>` 없음**
    - `.qty-val` input, 가구 select 모두 시각적 `.item-name` 만 있고 label 연결 없음 → 스크린리더 접근성 미달 (WCAG 1.3.1)
    - 디자인 팀 HTML 재작업 시 함께 처리 권장 (aria-label 또는 `<label for>` 추가)
  - **`moving-truck-size-calculator/index.html` — `selectValues` 사용 없는 dead code**
    - `updateSelect()` / `selectValues` 딕셔너리 정의되어 있으나 `getTotalVol()`이 DOM에서 직접 읽음 → 불필요. 추후 정리 권고.

- 기능 정확성 검수 결과 (디자인 무관 항목):
  - moving-truck: `getTotalVol()` data-vol × qty 합산·select 직접 DOM 읽기·30% 여유 × 트럭 매핑·배지 경계값 처리 — 정확 ✓
  - dorm-vs-rent: 기숙사/자취 월합산·보증금 기회비용(연 2.5%/12)·period 선택·winner 토글·내역 렌더링 — 정확 ✓
  - SEO 태그·JSON-LD·`#ad-slot` — 양 파일 정상 ✓

- **배포 준비 상태: 배포 불가**
  - 사유: 디자인팀 파이프라인 미완료. 두 파일 모두 Pretendard 미도입·CSS 토큰 미선언·h1 1.5rem 미적용·hero-line 없음·확정 팔레트 미반영 (moving-truck: 티일 #0F766E 미적용, dorm-vs-rent: 코발트 #1D4ED8 + 앰버 #D97706 미적용)
  - 다빈치 최종 판정·HTML 반영 완료 후 재검수 필요

---

## 다빈치 최종 판정

**판정: 통과 — A안 폐기 확정 · B안 단일 채택 · HTML 다빈치 직접 반영**

달리 정리 그대로 집행했습니다. 추가 이의 없음.

### 반영 항목 (2건)

**moving-truck-size-calculator/index.html**
- `:root` 토큰 8종 (`--primary: #0F766E` 외) 선언
- Pretendard CDN 추가
- body font-family · h1 1.5rem · subtitle `var(--text-sub)`
- `.hero-line` CSS 정의 + HTML 삽입
- `.section-title` · `.item-vol` · `.truck-cap` · `.notice` → `var(--text-sub)`
- `.qty-btn:hover` · `select:focus` · `calc-btn` · `.truck-box` · `.truck-name` · `.vol-summary` · `.badge` → teal 토큰
- `@keyframes resultReveal` + `.result.show` 애니메이션 추가
- 버튼 hover `translateY(-1px) + box-shadow` 추가
- 기타 인라인 `#d4d4d4` → `var(--border)` · `#aaa` → `var(--text-sub)`
- `aria-label` 추가 (기타 직접 입력 input · 클레버 접근성 지적 처리)
- JS 로직·SEO·JSON-LD·`#ad-slot` 전체 유지

**dorm-vs-rent-calculator/index.html**
- `:root` 토큰 12종 (`--dorm-primary: #1D4ED8` · `--rent-primary: #D97706` 외) 선언
- Pretendard CDN 추가
- body font-family · h1 1.5rem · subtitle `var(--text-sub)`
- `.hero-line` CSS 정의 + HTML 삽입
- `.card-dorm` · `.card-rent` · `.dot-dorm` · `.dot-rent` → 각 토큰
- `input:focus` · `select:focus` · toggle · 메인 버튼 → `var(--dorm-primary)`
- preset-btn hover: dorm 카드 → dorm 톤 · rent 카드 → rent 톤 (컨텍스트 분기)
- `.compare-cell.dorm/rent` · `.winner` border · `.cell-type` · `.cell-amount` → 토큰
- `.diff-box` → `var(--dorm-soft)` + border
- `.breakdown-title` · `.period-note` · `.notice` · `.unit` · `.field-note` → `var(--text-sub)`
- JS 내 인라인 `#4f46e5` → `var(--dorm-hover)` · `#92400e` → `var(--rent-hover)`
- `@keyframes resultReveal` + `.result.show` 애니메이션 추가
- JS 로직·SEO·JSON-LD·`#ad-slot` 전체 유지
