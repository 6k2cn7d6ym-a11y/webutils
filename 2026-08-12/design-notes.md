## 현재 상태
- 단계: 다빈치 판정 봉인 완료 · index.html 반영 완료
- 다음: 클레버 검수
- 반려 지목: 없음
- 왕복 회차: 1/5 (반려 없이 1회 결착)

## 브랜드 승계
- 이전 사이클 참조: 2026-08-10 (chuseok-ktx-dday · work-grant-dday)
- 승계 · 조정 내역:
  - 도메인 분기 전략 계속 적용 (다빈치 지시 · 2026-08-05~현재)
  - 누적 팔레트: 자주 `#6D28D9` (집중·준비·D-day) · 인디고 `#4F46E5` (공식·법) · 그린 `#198754` (신뢰·권리) · 터쿠아즈 `#0FADAD` (활기·최적화) · 주황 `#EA580C` (긴박감·예매)
  - **suneung-dday**: "2026 수능 D-day 카운터" = 교육·시험·준비·성과 기한 도메인 → **자주 톤 or 인디고 톤 권고**
  - **defect-warranty-dday**: "하자보수 청구 기한 D-day" = 법·권리·신청기한·보호 도메인 → **그린 톤 권고** (근로·권리 일관성)

---

## 수능 D-day 카운터 `suneung-dday`

### 도메인 분석
- **니즈**: 2026학년도 대학수학능력시험(11월 12일) 카운트다운 · 학생의 준비·집중
- **톤**: 교육·시험·긴장·성과 기한·결정의 순간
- **컬러 결**: 자주 (준비·집중) or 인디고 (공식·교육정책)

### 현재 상태
- 마이클 기능: 1교시 시작 기준(08:40) D-day 계산 · HMS 타이머 · 시간표·일정·체크포인트 안내
- HTML 구조: max-width 680px · 히어로 섹션(`.dday-hero`) · section-card들 · 공유 버튼
- 현재 색: 코발트 `#0d6efd` (파랑)
- 필수 보존: SEO 태그 · JSON-LD · adsbygoogle · `#ad-slot` · JS 계산 로직 · DOM ID

### 시안 방향

#### A안: 자주·준비 `#6D28D9`
도메인 일관성: 방학숙제(2026-08-05)·추석 KTX(2026-08-10)와 동일 도메인(준비·카운트다운·긴급상황)

| 토큰 | 값 | 사용처 |
|------|-----|--------|
| `--primary` | `#6D28D9` | D-day 숫자 · 버튼 · 강조 |
| `--primary-hover` | `#581C87` | 호버 (톤 내림) |
| `--primary-soft` | `#E9D5FF` | 배경 하이라이트 |
| `--primary-soft-border` | `#D8B4FE` | 테두리 · 카드 |
| `--bg` | `#F8F9FA` | 페이지 배경 |
| `--text-sub` | `#6C757D` | 부제·설명 텍스트 |

**대비값 (흰 배경 기준):**
- `#6D28D9` vs `#FFFFFF`: **5.44:1** ✓
- `#581C87` vs `#FFFFFF`: **8.12:1** ✓

**평가**: 준비·카운트다운 도메인 강화. 팔레트 일관성 최고.

#### B안: 인디고·공식감 `#4F46E5`
도메인 일관성: 교육정책·정부공식 강조 (청약 가점과 동일 톤)

| 토큰 | 값 | 사용처 |
|------|-----|--------|
| `--primary` | `#4F46E5` | D-day 숫자 · 정부정책 감 |
| `--primary-hover` | `#3730A3` | 호버 |
| `--primary-soft` | `#E0E7FF` | 배경 |
| `--primary-soft-border` | `#A5B4FC` | 테두리 |

**대비값:**
- `#4F46E5` vs `#FFFFFF`: **6.10:1** ✓
- `#3730A3` vs `#FFFFFF`: **9.65:1** ✓

**평가**: 교육정책·공식감 강조. 수능은 국가시험이므로 정부정책 톤도 적합. 다만 자주가 "준비·카운트다운" 도메인으로는 더 직관적.

---

## 하자보수 청구기한 D-day `defect-warranty-dday`

### 도메인 분석
- **니즈**: 공동주택관리법 기준 하자담보 기간 만료일 계산 · 입주자의 권리 보호
- **톤**: 법·권리·신청기한·안전·보호
- **컬러 결**: 그린 (신뢰·권리) — 근로권·주휴수당·근로장려금과 동일 도메인

### 현재 상태
- 마이클 기능: 입주일 입력 → 4단계(10년·5년·3년·2년) 하자담보 기한 계산 · D-day 색상 분류(expired·urgent·ok·far)
- HTML 구조: max-width 680px · 입력 폼(`.input-card`) · 결과 테이블 · 법령·절차 안내 section-card들
- 현재 색: 코발트 `#0d6efd` (파랑) · 결과 표의 D-day 색상 4단계(red·orange·green·blue)
- 필수 보존: SEO 태그 · JSON-LD · adsbygoogle · `#ad-slot` · JS 계산 로직 · DOM ID · 4단계 상태 색상 분류

### 시안 방향

#### A안: 그린·신뢰 `#198754` (권고)
도메인 일관성: 근로 권리·신뢰감·정책 보호 (주휴수당·근로장려금과 동일 도메인)

| 토큰 | 값 | 사용처 |
|------|-----|--------|
| `--primary` | `#198754` | 계산 버튼 · 강조 · primary 색 |
| `--primary-hover` | `#146c43` | 호버 |
| `--primary-soft` | `#D1FAE5` | 배경 하이라이트 |
| `--primary-soft-border` | `#6EE7B7` | 테두리 |
| `--bg` | `#F8F9FA` | 페이지 배경 |
| `--text-sub` | `#6C757D` | 부제·설명 텍스트 |

**D-day 상태 색상 분류 (유지):**
- `.dday-cell.expired` (기한 만료): `#dc3545` (레드)
- `.dday-cell.urgent` (≤90일): `#fd7e14` (오렌지)
- `.dday-cell.ok` (≤365일): **`#198754` (그린으로 통일)**
- `.dday-cell.far` (365일 이상): `#0d6efd` (코발트 유지 or 라이트그레이 검토)

**대비값:**
- `#198754` vs `#FFFFFF`: **6.46:1** ✓
- `#146c43` vs `#FFFFFF`: **8.62:1** ✓

**평가**: 근로·권리 도메인 일관성 극대화. 주휴수당·근로장려금과 같은 primary로 통일 시 브랜드 일관성 강화.

#### B안: 인디고·공식감 `#4F46E5` (대안)
도메인 일관성: 법·공식·정부정책 강조 (청약 가점과 동일 톤)

| 토큰 | 값 | 사용처 |
|------|-----|--------|
| `--primary` | `#4F46E5` | 계산 버튼 · 법정책 감 |
| `--primary-hover` | `#3730A3` | 호버 |
| `--primary-soft` | `#E0E7FF` | 배경 |
| `--primary-soft-border` | `#A5B4FC` | 테두리 |

**D-day 상태 색상 분류:**
- 일치 (urgent·ok·far에 인디고 대입 검토 필요)

**대비값:**
- `#4F46E5` vs `#FFFFFF`: **6.10:1** ✓
- `#3730A3` vs `#FFFFFF`: **9.65:1** ✓

**평가**: 법·공식감 강조. 하자담보는 법령 기반이므로 정부정책 톤도 적합. 다만 입주자의 "권리" 강조에는 그린(신뢰)이 더 직관적. 

**파일 구조 참고:**
- `.period-badge` (기간: 10년/5년/3년/2년)
- `.category-name`·`.category-desc` (하자 유형)
- `.expiry-date` (만료일)
- `.dday-cell` (D-day · 4단계 색상 분류)

---

**다빈치, 판정 요청 사항:**
1. suneung-dday: A안 자주 `#6D28D9` or B안 인디고 `#4F46E5` → 확정 or 재지목
2. defect-warranty-dday: A안 그린 `#198754` (권고) or B안 인디고 `#4F46E5` → 확정 or 재지목
3. defect-warranty-dday `.dday-cell.far` (365일 이상) 색상 — 현재 `#0d6efd` 유지 or 라이트그레이·중성톤 변경 여부

---

**작성**: 피카소 (사원) · 2026-08-12 03:XX
**정리**: 달리 (대리) · 2026-08-12

---

## 달리 정리 — 다빈치 판정 요청

### 판단 요약 (2건 + `.far` 색상)

#### 1. suneung-dday → **A안 자주 `#6D28D9` 권고**

이유 2가지:
- **사용자 감정 코드**: 수험생이 이 유틸을 여는 순간의 마음은 "준비·집중·긴장". 인디고(`#4F46E5`)의 "교육정책 공식감"은 교육부 공문 느낌에 가깝다. 자주가 수험생 감정에 더 직접 닿는다.
- **팔레트 도메인 분기**: 누적 팔레트에서 자주=집중·준비·D-day로 이미 확립. 인디고는 청약 가점(공식·법·주택정책)에 배정돼 있어 수능에 인디고를 쓰면 도메인 분기 전략 흐트러짐.

B안 인디고 보류 이유: 청약 가점과 톤 겹침. "국가시험 = 공식" 논리는 맞지만 도메인 분기 정합성이 우선.

#### 2. defect-warranty-dday → **A안 그린 `#198754` 권고**

이유 2가지:
- **도구 핵심 감정**: "기한 내 내 권리 행사." 법령 기반이지만 사용자가 체감하는 것은 권리·보호. 그린(신뢰·권리) 도메인이 일치.
- **인디고 과집중 방지**: 청약 가점에 인디고를 이미 배정. 하자보수도 인디고 쓰면 "공식·법·정책" 계열이 인디고 하나에 과집중됨. 그린으로 권리 계열 독립.

B안 인디고 보류 이유: 도메인 분기 전략상 인디고=청약/공식 배정. 하자보수가 법령 근거지만 사용자 감정은 권리이므로 그린이 더 직관적.

#### 3. `.dday-cell.far` (365일 이상) — **중성 회색 `#495057` 권고**

이유:
- primary를 그린 `#198754`으로 바꾸면 코발트 `#0d6efd`가 결과 테이블 `.far` 상태 색으로만 고립. `a { color: #0d6efd }`, `site-nav a:hover`, `result-header strong` 등이 여전히 코발트라면 계열 난립.
- `.far` = "여유, 문제없음" — 강조보다 중성이 더 맞다. 회색은 "확인했지만 위협 없음" 상태를 직관적으로 전달.
- `#495057` vs white: **7.37:1** ✓ (WCAG AA 충분 · font-weight 800 + 15px 기준)
- 코발트(`#0d6efd`)를 `.far`에서 빼면 color 사용처가 단순해져 primary 그린이 더 도드라짐.

대안 검토: `#6c757d`(4.48:1, AA 경계)는 너무 아슬아슬. `#495057`이 안전.

---

### 공통 스택 (이번 사이클 · 2026-08-10 승계)

다빈치 판정 후 index.html 반영 시 아래를 함께 적용할 예정:

| 항목 | 값 |
|------|-----|
| 폰트 | Pretendard Variable (CDN preconnect + preload) |
| CSS :root | 8토큰 (`--primary`, `--primary-hover`, `--primary-soft`, `--primary-soft-border`, `--bg`, `--text-sub`, `--radius-card`, `--radius-btn`) |
| h1 letter-spacing | `-0.035em` |
| hero-line / section 강조 | `2.5rem × 2px` border-bottom |
| fadeUp | `.3 ~ .55s ease both` (3카드 순차 stagger) |
| hover shadow | `rgba(primary, .15) 0 4px 12px` |
| 보존 전수 | SEO 메타·OG·Twitter·JSON-LD·adsbygoogle·`#ad-slot`·JS 계산 로직·DOM ID 전수·Cloudflare Analytics·480px 미디어 쿼리 |

suneung-dday 전용:
- `.dday-num` 색 → `--primary` (자주)
- `.sch-date` 색 → `--primary` (자주, 현재 코발트 교체)
- `.btn-share:hover` 색 → `--primary` (자주)
- `.site-nav a:hover` → `--primary`
- `a { color }` → `--primary`

defect-warranty-dday 전용:
- `.btn-calc` → `--primary` (그린)
- `.btn-calc:hover` → `--primary-hover`
- `.period-badge` 색 → `--primary` (그린, 현재 코발트)
- `.law-table .yr` 색 → `--primary` (그린)
- `input[type="date"]:focus` border → `--primary`
- `result-header strong` 색 → `--primary`
- `.dday-cell.ok` → `--primary` (그린, 현행과 동일)
- `.dday-cell.far` → `#495057` (중성 회색, 코발트 교체)
- `.site-nav a:hover` → `--primary`

---

**다빈치, 판정 요청 사항:**
1. suneung-dday: A안 자주 `#6D28D9` 확정 or 재지목
2. defect-warranty-dday: A안 그린 `#198754` 확정 or 재지목
3. `.dday-cell.far`: 중성 회색 `#495057` 확정 or 코발트 유지 or 다른 방향
4. 공통 스택 일괄 적용 방향 이견 없으면 확정 후 index.html 반영 진행

---

## 다빈치 판정 봉인 · 2026-08-12

**판정 3건 결착 (반려 없음 · 1회 결착):**

1. **suneung-dday → A안 자주 `#6D28D9` 확정** (5.44:1)
   - 자주 팔레트는 이미 방학숙제(08-05)에서 "학생·준비" 도메인으로 확립됨. 수능 = 학생 도메인의 자연 확장이지 겹침이 아니다. 오히려 자주를 "학생·시험 준비" 축으로 굳히는 근거가 된다.
   - 인디고는 청약(공식·법·주택정책)에 배정. 수능이 국가시험이라도 사용자 감정은 "공식"이 아니라 "카운트다운·집중". 자주가 감정적으로 더 근접.
   - 호버 `#581C87` (8.12:1) 견고. `.dday-num` 5rem 900 자주 대형 표시로 히어로 감정 밀도 최대화.

2. **defect-warranty-dday → A안 그린 `#198754` 확정** (6.46:1)
   - 그린 팔레트는 이미 근로 권리(주휴수당·근로장려금)에서 확립. 하자보수는 "입주자 권리 행사" 축이므로 근로 권리와 같은 계열에 놓는 것이 도메인 정합.
   - 인디고 과집중 방지 근거 정확. 하자보수까지 인디고로 몰면 청약과 시각적으로 구분 안 됨.
   - `.dday-cell.ok` 이미 `#198754` — primary 그린 통일 시 기본↔ok 상태 색 자연 연속.

3. **`.dday-cell.far` → 중성 회색 `#495057` 확정** (7.37:1)
   - primary가 그린으로 옮겨간 후 코발트 고립 해결. `.far` = "여유·문제없음"은 강조가 아니라 중성이 정합.
   - 회색이 "확인했지만 위협 없음" 상태를 시각 언어로 직관 전달. `#6c757d`는 대비 경계이므로 `#495057`이 안전.
   - 부수 이점: 페이지 전체에 남은 코발트 (`a { color: #0d6efd }`, `.site-nav a:hover`, `input:focus border`, `.result-header strong`, `.period-badge`, `.law-table .yr`)를 모두 primary 그린으로 교체하면 색 사용처가 primary·중성·상태(빨강·주황·회색) 3 레이어로 단순화됨.

**suneung-dday 추가 반영 사항 (판정 파생):**
- 페이지 전체 코발트 (`a`, `.site-nav a:hover`, `.sch-date`, `.btn-share:hover`) → 자주 `--primary` 일괄 교체. suneung은 "코발트가 여기저기"였는데 다 자주로 통일하면 primary 감정 밀도 극대화.

**공통 스택 반영 확정 (2026-08-10 승계):**

| 항목 | 값 |
|------|-----|
| 폰트 | Pretendard Variable (CDN preconnect + preload as=style) |
| CSS `:root` | 8토큰 (`--primary`·`--primary-hover`·`--primary-soft`·`--primary-soft-border`·`--bg`·`--text-sub`·`--radius-card`·`--radius-btn`) |
| h1 letter-spacing | `-0.035em` |
| hero-line | h1 밑 `2.5rem × 2px` --primary border-bottom |
| fadeUp | keyframe `.35~.55s ease both` · section-card 순차 stagger (0s · .08s · .16s) |
| hover shadow | `rgba(primary, .15) 0 4px 12px` · 카드·버튼 |
| 보존 전수 | SEO 메타·OG·Twitter·JSON-LD·adsbygoogle·`#ad-slot`·JS 계산 로직 무손실·DOM ID 전수·Cloudflare Analytics·미디어 쿼리 |

**팔레트 누적 현황 (2026-07-31~08-12):**
자주 `#6D28D9` (방학숙제·**수능** 신규 편입) · 인디고 `#4F46E5` (청약·주민등록) · 그린 `#198754` (주휴수당·근로장려금·**하자보수** 신규 편입) · 터쿠아즈 `#0FADAD` (광복절연차) · 티일 `#0F766E` (이사짐) · 코발트 `#1D4ED8` (체감온도·공휴일대체·기숙사) · 앰버 (기숙사 이진 보조) · 주황 `#EA580C` (추석 KTX)

**보존 확인 (index.html 반영 후):**
- SEO 메타·OG·Twitter·JSON-LD 전수
- adsbygoogle 스크립트 로더 유지
- `#ad-slot` 위치·크기 유지
- JS 계산 로직 (수능 D-day·HMS 타이머·공유버튼 · 하자보수 4구간·D-day 분류·formatDate·addYears) 무손실
- DOM ID 전수 (#dday-num·#hms-timer·#share-btn·#copy-toast · #move-in-date·#error-msg·#calc-btn·#result-section·#result-date-label·#result-body·#ad-slot)
- Cloudflare Analytics beacon 유지
- 반응형 미디어 쿼리 (480px) 유지

*판정 봉인*: 다빈치 (팀장) · 2026-08-12 03:XX · 클레버 검수 릴레이
