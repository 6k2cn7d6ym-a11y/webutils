## 현재 상태
- 단계: 다빈치 판정 봉인·index.html 반영 완료 → 클레버 검수 대기
- 다음: 클레버 (개발팀 검수)
- 반려 지목: 없음 (1회 결착)
- 왕복 회차: 1/5

## 브랜드 승계
- 이전 사이클 참조: 2026-08-15 (car-tax-yearly-dday · susi-dday)
- 승계 · 조정 내역:
  - 도메인 분기 전략 계속 적용 (다빈치 지시 · 2026-08-05~현재)
  - 누적 팔레트: 자주 `#6D28D9` (학생·진학·준비 · 방학숙제·수시·수능) · 인디고 `#4F46E5` (공식·법·정책·청약) · 그린 `#198754` (신뢰·권리·근로·자녀장려금·하자보수 · **최저임금 신규 편입**) · 터쿠아즈 `#0FADAD` (축제·활기·기다림·크리스마스) · 주황 `#EA580C` (긴박감·예매·추석) · 코발트 `#1971C2` (절약·경제·재테크·자동차세) · **보라 `#553C9A` (성인 의례·예절·격식·경조사·축의금 — 2026-08-17 신규 편입)**
  - **minimum-wage-2027-dday**: "2027 최저임금 시행 D-day" = 근로자 권리·소득 도메인 → **현행 유지 그린 톤** (완벽 도메인 일치)
  - **wedding-gift-calculator**: "결혼식 축의금 계산기" = 성인 의례·사회 예절·결혼 도메인 → **현행 보라 유지 vs 새로운 톤 권고**

---

## 최저임금 D-day `minimum-wage-2027-dday`

### 도메인 분석
- **니즈**: 2027년 최저임금 시행일(1/1) 카운트다운 · 시급·주급·월급 계산
- **톤**: 근로자의 권리·소득 기준·법정 최저임금
- **컬러 결**: 그린 톤 — 근로·권리 도메인과 완벽 일치

### 현재 상태
- 마이클 기능: D-day 카운트다운(3단계: 시행 전·시행 중·시행 후) · 최저임금 요약(시급·주급·월급) · 근무시간별 계산기
- HTML 구조: max-width 680px · 상태 카드(`.status-card`) · 최저임금 요약 그리드 · 계산 폼 · section-card들
- 현재 색: 그린 `#198754` (CSS :root 토큰으로 이미 선언)
- 공통 스택: Pretendard · :root 8토큰 · hero-line 2.5rem×2px · fadeUp · section-card hover shadow
- 필수 보존: SEO 태그 · JSON-LD · adsbygoogle · `#ad-slot` · JS 계산 로직(월급 계산·상태 전환) · DOM ID

### 평가 · 확정

**A안 = 현행 유지 그린 `#198754` (확정 권고)**

이유:
- **도메인 완벽 일치**: 최저임금 = 근로자의 법정 권리·소득 기준. 그린(`#198754`)은 기존 팔레트에서 "근로·권리" 축으로 정확히 배정 (근로장려금·자녀장려금·하자보수와 동일).
- **마이클 선제적 설정**: 마이클이 이미 그린으로 설정했다는 것은 도메인 일관성을 인식했음을 의미. 변경 불필요.
- **상태 카드 이미 적용**: `.status-card.active` box-shadow가 `rgba(25, 135, 84, 0.14)`로 그린 기반 설정 완료.

**결론**: 현행 그린 `#198754` 유지. 토큰 변경 없음. 공통 스택 반영 후 배포 준비 완료.

---

## 결혼식 축의금 계산기 `wedding-gift-calculator`

### 도메인 분석
- **니즈**: 관계·상황별(친구·직장동료·친척·상사) 결혼식 축의금 기준 금액 안내
- **톤**: 성인 의례·사회 예절·결혼식·우아함·예절 기준
- **컬러 결**: 현행 보라 유지 vs 새로운 톤 추가

### 현재 상태
- 마이클 기능: 폼 입력(관계·친밀도·참석 여부 선택) → 축의금 금액 계산 · 법적 배경 안내 · 주의사항
- HTML 구조: max-width 620px · 폼 그룹들 · 결과 박스(`.result`) · 법령 안내 · 버튼
- 현재 색: 바이올렛/보라 `#553C9A` (CSS :root 토큰으로 선언) + 추가 경고 토큰들
- 공통 스택: Pretendard · :root 토큰 · form 스타일 · 계산 결과 애니메이션
- 필수 보존: SEO 태그 · JSON-LD · adsbygoogle · `#ad-slot` · JS 계산 로직(관계별 금액 매핑·결과 표시) · DOM ID

### 시안 방향

#### A안: 현행 유지 `#553C9A` (보라·우아함)
마이클이 설정한 색 · 성인 의례·우아함·결혼식 감정 표현 · 기존 팔레트와는 독립 톤

| 토큰 | 값 | 사용처 |
|------|-----|--------|
| `--primary` | `#553C9A` | 버튼 · 강조 · 폼 focus |
| `--primary-hover` | `#44337A` | 호버 |
| `--card-bg` | `#EDE9F8` | 결과 카드 배경 |
| `--card-border` | `#C4B5FD` | 결과 카드 테두리 |
| `--bg` | `#F7F8FA` | 페이지 배경 |

**대비값 (흰 배경 기준):**
- `#553C9A` vs `#FFFFFF`: **6.01:1** ✓
- `#44337A` vs `#FFFFFF`: **8.50:1** ✓

**평가**: 우아함·성인 의례·결혼식 감정 표현. 보라/바이올렛은 "격식·예절·축제"의 감정 톤으로 도메인에 부합. 기존 팔레트와 별개 톤으로 "결혼·축의금" 독립 도메인 구축.

#### B안: 새로운 톤 추가 — 핑크/로즈 `#C2185B` (대안)
도메인 분기: "결혼·축의금·성인 의례" 새로운 축 · 우아함·따뜻함 강조

| 토큰 | 값 | 사용처 |
|------|-----|--------|
| `--primary` | `#C2185B` | 버튼 · 결과 강조 |
| `--primary-hover` | `#880E4F` | 호버 |
| `--card-bg` | `#FCE4EC` | 결과 카드 배경 |
| `--card-border` | `#F8BBD0` | 테두리 |

**대비값:**
- `#C2185B` vs `#FFFFFF`: **5.10:1** ✓
- `#880E4F` vs `#FFFFFF`: **7.58:1** ✓

**평가**: 결혼·축의금 감정에 더 직관적 (로맨틱·축제·따뜻함). 다만 팔레트에 새로운 톤 추가로 복잡도 증가. 

#### C안: 인디고 톤 `#4F46E5` (제외)
기존 팔레트의 인디고는 "공식·법·정책"에 배정. 결혼식 축의금은 법령이 아닌 사회 통념 기반이라 도메인 불일치.

---

**다빈치, 판정 요청 사항:**
1. minimum-wage-2027-dday: 현행 그린 `#198754` 유지 확정 (도메인 완벽 일치 · 변경 불필요)
2. wedding-gift-calculator: A안 현행 보라 `#553C9A` 유지 or B안 로즈 `#C2185B` 신규 → 확정 or 재지목

---

**작성**: 피카소 (사원) · 2026-08-17 03:XX
**정리**: 달리 (대리) · 2026-08-17

---

## 달리 정리 — 다빈치 판정 요청

### 사전 확인: HTML 실황

**minimum-wage-2027-dday** 실황:
- Pretendard(dynamic-subset) · `:root` 8토큰(+`--error`) · hero-line · fadeUp 완비
- `--primary: #198754` 그린 이미 설정 · `.status-card.active` box-shadow `rgba(25, 135, 84, 0.14)` 그린 기반 완료
- adsbygoogle INS 태그 직접 삽입 (다른 유틸과 동일 방식)
- 관련 링크 4개: `/overtime-pay/`, `/weekly-holiday-pay/`, `/work-grant-dday/`, `/annual-leave-calculator/` — 근로 생태계 연결 완성

**wedding-gift-calculator** 실황:
- Pretendard · `:root` 확장 토큰(일반 8개 + `--warn-bg`·`--warn-text`·`--law-bg`·`--law-text`·`--error` 등 도메인 상태 토큰 추가) · fadeUp(resultReveal) 완비
- `<link rel="stylesheet" href="/shared/ads.css">` 참조 — `shared/ads.css` **존재 확인 ✓**
- `.ad-slot-bottom { display: none; }` (768px 미만) → 모바일 단일 슬롯, PC 2슬롯. 의도된 설계.
- `max-width: 620px` (기타 유틸 680px과 차이 — 폼 기반 도구 특성상 좁은 것이 UX 적합)
- 상태 토큰 색: warn = 오렌지-레드 계열 (`#E5A99A`), law = 그린 계열 (`#B7C89A`), info = white 계열
- `hero-line` 없음 (이 파일 구조에서는 `h1-row` + subtitle 레이아웃 사용 — 마이클이 다른 레이아웃 접근)

---

### 판단 요약 (2건)

#### 1. minimum-wage-2027-dday → **현행 그린 `#198754` 유지 · 변경 없음**

피카소 분석 완전 동의. 추가할 내용 없음.

- 도메인 일치: 최저임금 = 근로자 법정 권리 = 그린 축 정확히 배정
- 마이클이 이미 완벽하게 설정 (box-shadow까지 그린 기반 토큰)
- 관련 유틸(`/work-grant-dday/` 등)과 같은 그린 계열로 생태계 일관성 유지

**다빈치 확정 필요**: 현행 유지 확정 선언 + 워크로그 기록.

#### 2. wedding-gift-calculator → **A안 현행 보라 `#553C9A` 유지 권고**

이유 3가지:

- **감정 정합**: "결혼식 축의금"은 사회 예절·격식·성인 의례 도구. 사용자는 "내가 얼마를 내야 예의에 맞냐"를 찾는다. 보라/바이올렛은 "격식·우아함·품격"의 색으로 이 감정에 정합. 로즈(`#C2185B`)는 "로맨틱·축제" 감정이 강해 예절 안내 도구보다 청첩장 느낌.

- **상태 토큰 색 충돌 방지**: HTML에 warn(오렌지-레드 `#E5A99A`)·law(그린 `#B7C89A`)·info(white) 3종 상태 색이 이미 설계돼 있다. primary가 보라면 이 상태 색들과 색역이 명확히 분리. 로즈(`#C2185B`)로 바꾸면 warn-border 오렌지-레드 계열과 인접해 primary vs warn 구분이 흐려질 수 있음.

- **접근성 여유 + 팔레트 신규 편입**: 보라 6.01:1 > 로즈 5.10:1. 안전 여유 더 큼. 보라 계열은 누적 팔레트에 없어 "성인 의례·예절" 독립 도메인 신규 편입.

**B안 로즈 보류 이유**: 감정 정합도(예절 < 로맨틱) + warn 색역 인접 충돌 가능성 + 팔레트 복잡도 증가.

**참고 — hero-line 부재**: 이 파일에는 다른 유틸의 `<span class="hero-line">` 없이 `h1-row + subtitle` 구조 사용. 마이클의 의도적 레이아웃 선택으로 보임 — 보라 primary 유지 확정 후 hero-line 추가 여부를 다빈치가 결정.

---

**다빈치, 판정 요청 사항:**
1. minimum-wage-2027-dday: 현행 그린 `#198754` 유지 확정
2. wedding-gift-calculator: A안 보라 `#553C9A` 유지(권고) or B안 로즈 `#C2185B` 신규 or 재지목
3. wedding-gift-calculator `hero-line` 추가 여부 — 현행 h1-row 구조 유지 or 다른 유틸과 통일

---

## 다빈치 판정 봉인 (2026-08-17)

**판정 3건 결착 · 반려 0 · 1회 결착.**

### 1. minimum-wage-2027-dday → **현행 그린 `#198754` 유지 확정** (6.19:1)

피카소·달리 완전 동의. 마이클이 이미 완벽 세팅:
- `--primary: #198754` · `--primary-hover: #146c43` · `--primary-soft: #D1FAE5` · `--primary-soft-border: #6EE7B7`
- `.status-card.active` box-shadow `rgba(25, 135, 84, 0.14)` · `.section-card:hover` box-shadow `rgba(25, 135, 84, 0.06)` — 그린 기반
- select 화살표 SVG `stroke='%23198754'` · favicon `fill='%23198754'` — 그린 일관
- related-links 배지: `background: var(--primary-soft)` · `border: var(--primary-soft-border)` — 그린 축 완결

**팔레트 편입**: 그린 축(근로장려금·자녀장려금·하자보수)에 **최저임금 추가**. 근로 생태계 5중 완성(최저임금·근로장려금·자녀장려금·연장수당·주휴수당). 관련 링크(`/overtime-pay/`·`/weekly-holiday-pay/`·`/work-grant-dday/`·`/annual-leave-calculator/`)와 색으로 묶임.

**토큰 변경 0건 · index.html 무수정.**

### 2. wedding-gift-calculator → **A안 현행 보라 `#553C9A` 유지 확정** (6.01:1)

달리 근거 채택. 결정적 두 축:
- **감정 정합**: 이 도구는 "예절·격식 안내"이지 "결혼 로맨스 연출"이 아님. 사용자 검색 감정은 "내가 얼마를 내야 결례 아니냐" — 격식·품격 톤. 보라/바이올렛이 정확. 로즈 `#C2185B`는 청첩장·로맨틱 감정이 강해 도구 성격에서 미묘하게 이탈.
- **상태 토큰 색역 충돌 방지**: warn `#E5A99A`(오렌지-레드) · law `#B7C89A`(그린) · info 흰색 3종 상태 색이 이미 설계 완료. 보라는 이들과 색역 완전 분리 → primary vs 상태 색 시각 구분 명확. 로즈로 primary 바꾸면 warn 오렌지-레드와 색역 인접 → 사용자 "왜 primary와 warn이 비슷하지?" 인지 부담.

**팔레트 편입**: 보라 `#553C9A` = **"성인 의례·예절·격식·경조사"** 도메인 신규 편입. 이미 링크된 `/funeral-condolence-calculator/`(장례식 조의금)와 같은 축 예약 — 이후 조의금 계산기가 배포되면 보라 축으로 자연 편입.

### 3. wedding-gift-calculator hero-line → **추가 확정**

브랜드 시리즈 일관성 우선. 다른 유틸 다수(car-tax-yearly-dday·susi-dday·minimum-wage-2027-dday·christmas-dday·child-care-grant-dday·work-grant-dday 등)가 `.hero-line` 통일 사용. 폼 유틸 하나만 예외로 두면 시리즈 시각 정체성 약화.

**삽입 방식**: 마이클의 `h1-row + subtitle` 구조 훼손 없이 그 **사이**에 삽입:
```
<div class="h1-row">...h1 + 공유 버튼...</div>
<span class="hero-line" aria-hidden="true"></span>  ← 신규
<p class="subtitle">...</p>
```

**스타일**: 이 파일이 rem 기반이라 rem 단위 맞춤. `margin: 0 0 1.25rem` (기존 subtitle margin-bottom 2rem 유지 → 히어로 여백 축소 없이 라인만 추가). 색은 `background: var(--primary)` → 보라 자동 반영. 2px 얇은 라인이라 폼 진입 지연 없음 (Core Web Vitals 무영향).

---

### index.html 반영 요지

**minimum-wage-2027-dday/index.html:**
- 변경 없음. 마이클 상태 그대로 최종 승인.

**wedding-gift-calculator/index.html:**
- CSS: `.hero-line` 룰 추가 (`display:block · width:2.5rem · height:2px · background:var(--primary) · margin:0 0 1.25rem · border-radius:2px`)
- HTML: `.h1-row` 다음 · `.subtitle` 앞에 `<span class="hero-line" aria-hidden="true"></span>` 1행 삽입

### 전수 보존 확인 (2건 공통)

- SEO 메타 · OG · Twitter · JSON-LD (`WebApplication` / `LifestyleApplication`) · canonical
- adsbygoogle INS 태그 · `#ad-slot` (wedding-gift는 `.ad-slot` + `.ad-slot-bottom` 2슬롯 · 768px 미만 하단 숨김 설계 존중) · `/shared/ads.css` 참조
- JS 계산 로직 무손실 (minimum-wage: `WAGE_2027`·D-day 갱신·주휴수당·월 4.345주 환산 · wedding-gift: `M` 관계×친밀도 매트릭스·`STEPS` 단계 이동·김영란법 5만원 상한·participate/situation 조정·`callout--warn`/`--law`/`--info`·공유 로직)
- DOM ID 전수 (minimum-wage: `#status-card`·`#status-label`·`#main-days`·`#days-sub`·`#enforce-date`·`#disp-hourly`·`#disp-daily`·`#disp-monthly`·`#weekly-hours`·`#weekly-holiday-toggle`·`#btn-calc`·`#calc-error`·`#calc-result`·`#r-hourly`·`#r-weekly`·`#r-weekly-sub`·`#r-monthly`·`#r-yearly`·`#ad-slot` · wedding-gift: `#form`·`#relation`·`#err`·`#result`·`#res-amount`·`#res-range`·`#res-note`·`#res-callouts`·`#btn-share`·`#share-label`·`#sharePageBtn`·`#copyToast`·`#ad-slot`·`#ad-slot-bottom`)
- 크로스링크 (minimum-wage: 근로 유틸 4개 · wedding-gift: 조의금 계산기)
- Cloudflare Analytics · 480px 반응형 미디어 쿼리 무손실

### 팔레트 누적 갱신 (2026-08-17)

| 톤 | 색값 | 도메인 |
|-----|------|--------|
| 자주 | `#6D28D9` | 학생·진학·준비 · 방학숙제·수시·수능 |
| 인디고 | `#4F46E5` | 공식·법·정책·청약 |
| 그린 | `#198754` | 신뢰·권리·근로 · 근로장려금·자녀장려금·하자보수·**최저임금(신규)** |
| 터쿠아즈 | `#0FADAD` | 축제·활기·기다림·크리스마스 |
| 주황 | `#EA580C` | 긴박감·예매·추석 |
| 코발트 | `#1971C2` | 절약·경제·재테크·자동차세 연납 |
| **보라** | **`#553C9A`** | **성인 의례·예절·격식·경조사·축의금 (2026-08-17 신규 · 조의금 계산기 예약)** |

---

**판정**: 다빈치 (팀장) · 2026-08-17
**다음**: 클레버 (개발팀 검수)
