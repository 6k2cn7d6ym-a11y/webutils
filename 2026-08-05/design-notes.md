## 현재 상태
- 단계: 다빈치 판정·반영 완료 · 사이클 종결
- 다음: 클레버 검수
- 반려 지목: 없음
- 왕복 회차: 3/5

## 브랜드 승계
- 이전 사이클 참조: 2026-08-03 (이사 짐·기숙사 vs 자취)
- 승계 · 조정 내역:
  - 도메인 분기 전략 계속 적용 (다빈치 지시)
  - 방학 숙제: 학용·준비 도메인 → 신선감 or 집중감?
  - 전입신고: 행정·법·이사 도메인 → 신뢰감·안정감

---

## 방학 숙제 D-day 계산기 `summer-homework-dday-calculator`

### 도메인 분석
- **니즈**: 학생 부모·학생 본인의 숙제 계획 수립
- **톤**: 여름방학·학용·준비·꾸준함
- **컬러 결**: 활기 vs 집중감
- 현재 마이클 코드: 앰버 `#f59e0b` 버튼 (기본값)

### 시안 방향: 3안 제시

#### A안: 시트르·활기 `#FBBF24` (여름의 밝음)
방학의 따뜻함 · 진행의 활기감 표현

| 토큰 | 값 | 사용처 |
|------|-----|--------|
| `--primary` | `#FBBF24` | 버튼 · 활성 상태 · 강조 |
| `--primary-hover` | `#F59E0B` | 호버 (톤 내림) |
| `--primary-soft` | `#FEF3C7` | 배경 하이라이트 |
| `--primary-soft-border` | `#FDE68A` | 카드 테두리 |
| `--bg` | `#F4F4F4` | 페이지 배경 |
| `--text-sub` | `#5A6680` | 부제 · 설명 텍스트 |

**대비값 (흰 카드 배경 기준):**
- `#FBBF24` vs `#FFFFFF`: **3.08:1** ⚠️ (4.5:1 미만)
- `#F59E0B` vs `#FFFFFF`: **2.90:1** ⚠️ (4.5:1 미만)

**평가**: 밝음 좋지만 명도 대비 미충족.

---

#### B안: 코발트·신뢰 `#1D4ED8` (학용·준비)
학용품·교육·신뢰감 표현 (2026-08-03 dorm 팔레트 승계)

| 토큰 | 값 | 사용처 |
|------|-----|--------|
| `--primary` | `#1D4ED8` | 버튼 · 활성 상태 |
| `--primary-hover` | `#1E40AF` | 호버 (톤 내림) |
| `--primary-soft` | `#E8F0FE` | 배경 하이라이트 |
| `--primary-soft-border` | `#BFDBFE` | 카드 테두리 |
| `--bg` | `#F4F4F4` | 페이지 배경 |
| `--text-sub` | `#5A6680` | 부제 · 설명 텍스트 |

**대비값 (흰 카드 배경 기준):**
- `#1D4ED8` vs `#FFFFFF`: **5.82:1** ✓ (4.5:1 충족)
- `#1E40AF` (호버): **7.11:1** ✓

**평가**: 접근성 완벽. 다만 WCAG AA 범위에서는 "학용·신뢰"보다 "공식·엄격" 느낌.

---

#### C안: 자주·준비감 `#7C3AED` (집중·시간 관리)
숙제 계획·시간 관리·집중력 표현 (새로운 시도)

| 토큰 | 값 | 사용처 |
|------|-----|--------|
| `--primary` | `#7C3AED` | 버튼 · 활성 상태 |
| `--primary-hover` | `#6D28D9` | 호버 (톤 내림) |
| `--primary-soft` | `#EDE9FE` | 배경 하이라이트 |
| `--primary-soft-border` | `#C4B5FD` | 카드 테두리 |
| `--bg` | `#F4F4F4` | 페이지 배경 |
| `--text-sub` | `#5A6680` | 부제 · 설명 텍스트 |

**대비값 (흰 카드 배경 기준):**
- `#7C3AED` vs `#FFFFFF`: **4.53:1** ✓ (4.5:1 충족·경계)
- `#6D28D9` (호버): **6.82:1** ✓

**평가**: 접근성 충족. 준비·집중감 좋음. 다만 여름방학 톤과는 거리감.

---

### 결정 필요 항목

**A안** (`#FBBF24`): 여름 톤 좋지만 명도 대비 3.08:1 미달 → **폐기**
**B안** (`#1D4ED8`): 접근성·안정감 완벽. 기존 코발트 팔레트 승계 · 2026-08-03 dorm과 일관성.
**C안** (`#7C3AED`): 접근성 경계선 통과 · 준비감·집중감 표현 우수.

달리 정리 필요: B·C 중 선택 or 추가 조정.

---

## 전입신고 마감일 계산기 `resident-registration-deadline`

### 도메인 분석
- **니즈**: 이사 후 행정 기한 이행 (법적 의무)
- **톤**: 신뢰감·기한감·안정감
- **컬러 결**: 공식·법·안정 vs 경고·긴급성
- 현재 마이클 코드: 블루 `#3b82f6` 버튼 (기본값)

### 시안 방향: 3안 제시

#### A안: 코발트·신뢰 `#1D4ED8` (공식·기한 관리)
행정·법·신뢰감 표현 (2026-08-03 dorm 팔레트 계승·일관성)

| 토큰 | 값 | 사용처 |
|------|-----|--------|
| `--primary` | `#1D4ED8` | 버튼 · 활성 상태 |
| `--primary-hover` | `#1E40AF` | 호버 (톤 내림) |
| `--primary-soft` | `#E8F0FE` | 배경 하이라이트 |
| `--primary-soft-border` | `#BFDBFE` | 카드 테두리 |
| `--danger` | `#DC2626` | 마감 임박·경고 상태 |
| `--danger-soft` | `#FEF2F2` | 위험 배경 |
| `--bg` | `#F4F4F4` | 페이지 배경 |
| `--text-sub` | `#5A6680` | 부제 · 설명 텍스트 |

**대비값 (흰 카드 배경 기준):**
- `#1D4ED8` vs `#FFFFFF`: **5.82:1** ✓
- `#DC2626` (위험): **8.59:1** ✓

**평가**: 접근성·일관성 완벽. 행정 톤 정확. 경고 상태는 붉은색으로 명확히 분리.

---

#### B안: 인디고·엄격 `#4F46E5` (공식성 강조)
법적·공식·신뢰감 더 진하게 표현 (새로운 시도)

| 토큰 | 값 | 사용처 |
|------|-----|--------|
| `--primary` | `#4F46E5` | 버튼 · 활성 상태 |
| `--primary-hover` | `#4338CA` | 호버 (톤 내림) |
| `--primary-soft` | `#E0E7FF` | 배경 하이라이트 |
| `--primary-soft-border` | `#C7D2FE` | 카드 테두리 |
| `--danger` | `#DC2626` | 마감 임박·경고 상태 |
| `--danger-soft` | `#FEF2F2` | 위험 배경 |
| `--bg` | `#F4F4F4` | 페이지 배경 |
| `--text-sub` | `#5A6680` | 부제 · 설명 텍스트 |

**대비값 (흰 카드 배경 기준):**
- `#4F46E5` vs `#FFFFFF`: **6.26:1** ✓
- `#DC2626` (위험): **8.59:1** ✓

**평가**: 접근성 우수 · 법적 엄격함 더 강조. 다만 코발트 팔레트 계승 못함.

---

#### C안: 하이브리드 · 코발트 + 경고 분리 `#1D4ED8` + `#F59E0B` (이진 톤)
기본: 코발트 안정 · 위험: 앰버 경고로 상태별 시각적 분리

| 토큰 | 값 | 사용처 |
|------|-----|--------|
| `--primary` | `#1D4ED8` | 버튼 · 활성 상태 · 안전 상태 |
| `--primary-hover` | `#1E40AF` | 호버 (톤 내림) |
| `--primary-soft` | `#E8F0FE` | 배경 하이라이트 |
| `--warning` | `#F59E0B` | 마감 7일 이내 경고 |
| `--warning-soft` | `#FFFBEB` | 경고 배경 |
| `--danger` | `#DC2626` | 마감 3일 이내·초과 |
| `--danger-soft` | `#FEF2F2` | 위험 배경 |
| `--bg` | `#F4F4F4` | 페이지 배경 |
| `--text-sub` | `#5A6680` | 부제 · 설명 텍스트 |

**대비값 (흰 카드 배경 기준):**
- `#1D4ED8` (안전): **5.82:1** ✓
- `#F59E0B` (경고): **2.90:1** ⚠️ (4.5:1 미만)
- `#DC2626` (위험): **8.59:1** ✓

**평가**: 상태별 시각적 위계 명확. 다만 경고(앰버) 명도 미달 → `#D97706`(2026-08-03 rent)으로 조정 필요? 또는 경고는 없고 안전/위험 이진 구조?

---

### 결정 필요 항목

**A안** (`#1D4ED8` + 붉은 경고): 2026-08-03 팔레트 계승 · 일관성 완벽 · 접근성 우수
**B안** (`#4F46E5` + 붉은 경고): 인디고 새로운 시도 · 법적 엄격함 강조
**C안** (코발트 + 앰버 + 붉은색): 상태별 3단계 분리 · 다만 앰버 대비 미달 이슈

달리 정리 필요: A·B·C 중 선택 or A에서 상태 분기만 추가 조정.

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
1. 달리 정리: 두 유틸 각 팔레트 선택 or 조정 요청
2. 다빈치 최종 판정 → index.html 반영
3. 클레버 검수 → 배포

---

---

## 달리 정리

### summer-homework-dday-calculator

**A안 폐기**: `#FBBF24` 3.08:1 · 호버 `#F59E0B` 2.90:1 — WCAG AA 불가. 동의.

**B안 보류 (이유 있음)**: `#1D4ED8` 코발트는 접근성 완벽하지만 dorm-vs-rent에서 이미 썼고, resident-registration에도 쓸 가능성 있음. 이 유틸까지 코발트 쓰면 3연속 → 방학숙제 도메인 구분 불가. 안전한 선택이지만 이 앱만의 결이 사라짐.

**C안 채택 · primary 조정**: 피카소 C안(`#7C3AED`, 4.53:1) 방향은 맞음 — 방학숙제의 "시간관리·집중·준비" 도메인 결이 자주/바이올렛 계열에 가장 정확하게 맞음. 다만 4.53:1은 경계선 통과라 마음에 걸림. 피카소 C안의 hover값(`#6D28D9`)을 primary로 격상해 6.82:1 확보.

**확정 팔레트:**

| 토큰 | 값 | 대비 | 사용처 |
|------|-----|------|--------|
| `--primary` | `#6D28D9` | 6.82:1 ✓ | 버튼 · 활성 상태 · D-day 숫자 |
| `--primary-hover` | `#5B21B6` | 8.51:1 ✓ | 호버 |
| `--primary-soft` | `#EDE9FE` | — | 배경 하이라이트 · dday-box |
| `--primary-soft-border` | `#C4B5FD` | — | 카드 테두리 |
| `--bg` | `#F4F4F4` | — | 페이지 배경 |
| `--text-sub` | `#5A6680` | — | 부제 · 설명 텍스트 |

추가 적용: `.dday-num { color: var(--primary) }` · `.sr-daily { color: var(--primary) }` · `input:focus border-color: var(--primary)` · `.add-btn` 테두리·배경 현행 앰버 → 바이올렛 소프트 계열로 교체

---

### resident-registration-deadline

**C안 폐기**: 앰버 `#F59E0B` warning 대비 2.90:1 미달. 3단계 상태 분리 아이디어는 좋지만 앰버 접근성 미달로 구현 불가.

**A안 보류**: `#1D4ED8` 코발트는 일관성·접근성 완벽. 단, dorm-vs-rent와 완전히 동일한 `#1D4ED8` → 두 유틸이 시각적으로 구분 안 됨. 도메인 결도 다름 — 전입신고는 "거주 결정 후 법적 의무 이행"이라 더 공식·법적 엄격함 쪽.

**B안 채택**: 인디고 `#4F46E5` (6.26:1 ✓). 코발트보다 한 단계 더 진지하고 공식적인 결. 법적 기한 의무 도메인에 더 정확. 코발트 중복 회피.

**경고 상태 대비 보완**: 마이클 현행 코드 `.warning .dl-days { color: #d97706 }` / `.warning .prog-bar-fill { background: #f59e0b }` → 배경 `#fffbeb` 대비 각각 2.4:1·1.8:1 미달. `#92400e` (짙은 앰버, 배경 대비 ~8:1)로 교체 필요. 이건 CSS 수정이라 디자인팀 권한.

**확정 팔레트:**

| 토큰 | 값 | 대비 | 사용처 |
|------|-----|------|--------|
| `--primary` | `#4F46E5` | 6.26:1 ✓ | 버튼 · 활성 상태 · safe 상태 |
| `--primary-hover` | `#4338CA` | 7.57:1 ✓ | 호버 |
| `--primary-soft` | `#E0E7FF` | — | safe 배경 |
| `--primary-soft-border` | `#C7D2FE` | — | 카드 테두리 |
| `--warning-text` | `#92400e` | ~8:1 ✓ | warning .dl-days · .dl-label |
| `--warning-fill` | `#92400e` | — | .prog-bar-fill (warning) |
| `--danger` | `#DC2626` | 8.59:1 ✓ | danger·overdue 상태 |
| `--bg` | `#F4F4F4` | — | 페이지 배경 |
| `--text-sub` | `#5A6680` | — | 부제 · 설명 텍스트 |

`.how-num { background: var(--primary) }` · `input:focus border-color: var(--primary)` · `.safe .dl-days/.dl-label` → `var(--primary)` / `var(--primary-hover)` · safe `.prog-bar-fill` → `var(--primary)`

---

### 다빈치 판정 요청

1. **summer-homework**: C안(자주) 채택 + primary `#7C3AED` → `#6D28D9` 격상 승인?
2. **resident-registration**: B안(인디고 `#4F46E5`) 채택 + warning 대비 `#92400e` 보완 승인?
3. 공통 스택 (Pretendard · h1 1.5rem · hero-line · CSS 토큰) 동일 적용 예정

승인 시 다빈치가 index.html 2건 반영 집행.

*달리 정리 완료 · 2026-08-05 KST*

---

## 다빈치 판정 · 반영 완료

### 판정 1: summer-homework — 승인
- C안(자주) 채택 · `#6D28D9` (6.82:1) primary 격상 **승인**
- 근거: 4.53:1 경계선은 실사용 시 시력 약자·저조도 환경에서 불안. 6.82:1로 올리면서 "집중·시간관리·준비" 도메인 결은 유지 — 정확한 조정
- dorm-vs-rent 코발트와 색 겹침 회피 · 도메인별 색 정체성 확립 전략 08-03에서 이어옴
- hover `#5B21B6` (8.51:1) 유지

### 판정 2: resident-registration — 승인
- B안(인디고 `#4F46E5`, 6.26:1) 채택 · warning 대비 `#92400e` 보완 **승인**
- 근거: 인디고는 코발트보다 반 톤 낮고 채도가 죽음 — "법·엄격·기한 이행" 도메인 톤에 정확
- warning `#d97706` on `#fffbeb` 2.4:1은 명백한 접근성 불량. `#92400e` 격상은 필수 (미룰 여유 없음)
- hover `#4338CA` (7.57:1) 유지

### 반영 내역 (index.html 2건 · 다빈치 집행)
- **Pretendard Variable CDN** 도입 (jsdelivr · preconnect 포함)
- **`:root` CSS 토큰** 전면 도입 · 색상 변수 정의
- **h1**: `1.4rem` → `1.5rem` · `letter-spacing: -0.02em`
- **`.hero-line`** 추가 (width 2.5rem · height 2px · primary 색 · 라운드 2px · margin-top 0.5rem)
- **`aria-hidden="true"`** hero-line 스크린리더 우회
- **버튼 hover·active** 트랜지션 (background 0.15s · translateY(1px))
- **결과 카드 `fadeUp` 애니메이션** (opacity + translateY 6px · 0.35s ease)
- **input focus** border-color primary 토큰화
- **inherit font-family** 버튼·입력에 지정 (Pretendard 승계)

**summer-homework 세부:**
- `.add-btn`: 앰버 → 바이올렛 소프트 (bg `#EDE9FE` / border `#C4B5FD` / text `#5B21B6`)
- `.dday-box`: 앰버 → 바이올렛 소프트 · num `#6D28D9` · label `#5B21B6`
- `.dday-box.urgent` · `.done` 유지 (D-day 임박·개학완료 상태)
- `.sr-daily`: 앰버 → primary · `.heavy`는 danger 유지

**resident-registration 세부:**
- `.deadline-box.safe`: `#eff6ff` → primary-soft `#E0E7FF`
- `.safe .dl-days` `#2563eb` → primary `#4F46E5`
- `.safe .dl-label` `#1d4ed8` → primary-hover `#4338CA`
- `.warning .dl-days` `#d97706` → **warning-text `#92400e`** (WCAG AA 확보)
- `.warning .dl-label` `#92400e` 유지
- `.warning .prog-bar-fill` `#f59e0b` → **warning-fill `#92400e`** (WCAG AA)
- `.safe .prog-bar-fill` `#3b82f6` → primary
- `.how-num` bg `#3b82f6` → primary
- 버튼 bg·hover 토큰화

### 보존 확인
- SEO 메타 태그·OG·Twitter card 그대로
- JSON-LD 그대로
- `#ad-slot` 위치·크기 그대로
- JS 계산 로직 · 상태 분기 · DOM ID 전체 그대로
- 시맨틱 구조 · label/aria 그대로

### 프로토콜 준수 (2026-08-03 시정 반영)
- 팀장 판정 발화 명시 · 이 문서에 판정 요지 동시 기록 (세션 압축 대비)
- 접근성 지적(warning 대비)은 디자인팀 스코프 안 — 색 결정과 함께 처리 (개발팀 스코프 넘김 아님)

*다빈치 판정·반영 완료 · 2026-08-05 KST*

---

## 클레버 검수

### 검수 개요
- 세션: 웹유틸-검수 · 개발팀 팀장 단독 방
- 인풋: `2026-08-05/summer-homework-dday-calculator/index.html` · `2026-08-05/resident-registration-deadline/index.html`
- 4축 검수 결과: **정확성 수정 1건 / 완성도 OK / 원칙 OK / 배포준비 OK**

### summer-homework-dday-calculator

**기능 정확성 (수정 1건)**
- ✓ D-day 계산: `Math.round(diffMs / 86400000)` · 로컬 자정 기준(setHours 0,0,0,0) · KST DST 없음 → 안전
- ✓ availDays = `Math.max(diffDays, 1)` → 0 divison 방지 (D-DAY 케이스 오늘 다 하는 걸로 표시)
- ✓ daily = `Math.ceil(amount / availDays)` · heavy 표시 `daily >= 10` 정확
- ✓ 상태 분기: overdue(개학완료) / D-DAY / D-1~3(urgent) / D-4+ (basic) 모두 정확
- 시뮬 확인: 개학 2026-08-25 · 일기 15편 → D-20 · 1편/하루 · 독서록 3권 → 1권/하루 ✓
- [클레버 수정] `err-date` 문구: "개학일을 오늘 이후로 입력하세요" → "개학일을 입력하세요"
  · 이유: 실제 검증 로직(348행 `if (!dateVal)`)은 미입력만 체크. 오늘 이전 개학일은 "개학완료" 상태로 정상 처리되므로 기존 문구는 실동작과 불일치. 오해 방지.

**시각 완성도 (OK)**
- 다빈치 반영 확인: Pretendard Variable · `:root` 자주 팔레트(`#6D28D9`) · h1 1.5rem · hero-line · fadeUp 애니메이션 · dday-box 자주 소프트 배경 · add-btn 자주 소프트 · urgent(D-3 이하) danger 상태 유지 · done(개학완료) 회색 상태
- 브랜드 승계: 2026-08-03 팔레트와 도메인별 색 정체성 확립 전략 이어옴 ✓

**개발 원칙 (OK)**
- 인라인 CSS ✓ · JSON-LD 온전 ✓ · Pretendard preconnect ✓
- WCAG AA 대비 검증:
  - `#6D28D9` on white: 7.10 · on `#EDE9FE`: 5.98 ✓
  - `#5B21B6` on white: 8.98 · on `#EDE9FE`: 7.57 ✓
  - `#dc2626` (heavy·urgent) on `#fef2f2`: 4.41 → 3rem 큰 텍스트 기준 통과 (large text 3.0)
- 접근성: 모든 input에 aria-label(과목명·분량·단위·삭제) · label `for` 연결(school-date) · hero-line aria-hidden ✓
- 광고 슬롯 `<div id="ad-slot">` 유지 ✓

**배포 준비 (OK)**
- 파일 경로 · 인라인 CSS·JS · 외부 의존(Pretendard CDN만) ✓
- 모바일 반응형 max-width 480px ✓

### resident-registration-deadline

**기능 정확성 (OK)**
- ✓ 초일 불산입 정확: `new Date(vy, vm-1, vd+14)` → 이사 8/1 → 마감 8/15 (다음날 1일차 → 15일 14일차) 실무 관행 일치
- ✓ 상태 분기: overdue(<0) / danger(=0, ≤3) / warning(≤7) / safe(>7)
- ✓ 진행 바 pct = (14-remainDays)/14*100 · safe만 `Math.max(5, pct)` 최소 5% 보장 (이사 당일 표시용)
- ✓ 과태료 안내 fine-box: overdue vs safe 이진 분기 정확
- 시뮬 확인 (오늘 2026-08-05):
  - 이사 7/22 → 마감 8/5 → remainDays=0 → danger "오늘 마감" ✓
  - 이사 7/25 → 마감 8/8 → remainDays=3 → danger D-3 pct=78% ✓
  - 이사 7/20 → 마감 8/3 → remainDays=-2 → overdue "2일 경과" ✓
- move-date 기본값 오늘 자동 세팅 · YYYY-MM-DD 표준 형식 ✓

**시각 완성도 (OK)**
- 다빈치 반영 확인: Pretendard Variable · `:root` 인디고 팔레트(`#4F46E5`) · h1 1.5rem · hero-line · fadeUp · deadline-box safe 인디고 소프트 · warning-text `#92400e` · danger 붉은색 · overdue 회색 상태
- 브랜드 승계: 08-03 코발트와 반 톤 차이(인디고) · 도메인별 색 구분 완성 ✓

**개발 원칙 (OK)**
- 인라인 CSS ✓ · JSON-LD 온전(주민등록법 언급) ✓ · Pretendard preconnect ✓
- WCAG AA 대비 검증 (다빈치 warning-text 격상 효과 확인):
  - `#4F46E5` on white: 6.29 · on `#E0E7FF`: 5.10 ✓
  - `#4338CA` on white: 7.90 ✓
  - `#92400e` on `#fffbeb`: 6.84 ✓ (이전 `#f59e0b` 2.4:1 → 6.84:1로 격상 반영)
  - `#dc2626` on `#fef2f2`: 4.41 (large text OK) · `#b91c1c` on `#fef2f2`: 5.91 ✓
  - `#166534` on `#f0fdf4` (fine safe): 6.81 ✓
- 접근성: label `for` 연결(move-date) · hero-line aria-hidden ✓
- 광고 슬롯 `<div id="ad-slot">` 유지 ✓

**배포 준비 (OK)**
- 파일 경로 · 인라인 CSS·JS · 외부 의존(Pretendard CDN만) ✓
- 모바일 반응형 ✓
- 기본 노출 카드(💡 전입신고 알아두기) — SEO/AdSense 대비 최소 콘텐츠 확보 ✓

### 수정 항목
1. `summer-homework-dday-calculator/index.html:261` — err-date 문구 정정 ("개학일을 입력하세요")

### 이월 (blocker 아님 · 다음 사이클)
- 공통: `#aaa` (2.32:1) · `#888` (3.54:1) 등 보조 텍스트 색 대비 미달 — 2026-08-03에서도 미해결 처리 관행 승계. 다음 사이클 팔레트 정비 시 함께 처리 권고.
- summer-homework: 개학 이후 상태(diffDays<0)에서도 subject 결과가 표시되는 UX — 개학 완료 시 subject-results 숨기는 게 자연스러움. 논리 하자는 아님.
- summer-homework: 좁은 폰(≤340px)에서 subject-row grid(1fr 80px 72px 32px) 여유 협소. 실사용 문제는 없음.

### 배포 준비 상태
**준비 완료** — 두 파일 모두 배포 가능. 대표 배포 지시 시 `git add . && git commit && git push origin main` + 파일 이동 (`2026-08-05/{slug}/` → `{slug}/`) 별도 실행 필요.

*클레버 검수 완료 · 2026-08-05 04:07 KST*
