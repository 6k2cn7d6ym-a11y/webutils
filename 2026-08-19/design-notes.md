## 현재 상태
- 단계: 다빈치 판정 봉인·index.html 반영 완료 → 클레버 검수 대기
- 다음: 클레버 (개발팀 검수)
- 반려 지목: 없음 (1회 결착)
- 왕복 회차: 1/5

## 브랜드 승계
- 이전 사이클 참조: 2026-08-17 (minimum-wage-2027-dday · wedding-gift-calculator)
- 승계 · 조정 내역:
  - 도메인 분기 전략 계속 적용
  - 누적 팔레트: 자주 `#6D28D9` (학생·진학·준비 · 방학숙제·수시·수능·**국가장학금 신규 편입**) · 인디고 `#4F46E5` (공식·법·정책·청약) · 그린 `#198754` (신뢰·권리·근로·자녀장려금·하자보수·최저임금) · 터쿠아즈 `#0FADAD` (축제·활기·기다림·크리스마스) · 주황 `#EA580C` (긴박감·예매·추석) · 코발트 `#1971C2` (절약·경제·재테크·자동차세) · 보라 `#553C9A` (성인 의례·예절·격식·경조사·축의금) · **스카이블루 `#0369A1` (교통·공공 서비스·복지 혜택·경로우대 지하철 — 2026-08-19 신규 편입)**
  - 공통 스택: Pretendard Variable · `:root` 8토큰 · h1 letter-spacing -0.03em · hero-line 2.5rem×2px · fadeUp · section-card hover shadow

---

## national-scholarship-dday (국가장학금 신청 D-day)

### 실황 확인

- **primary**: `#7C3AED` (밝은 바이올렛)
- **primary-hover**: `#6D28D9` ← 기존 교육 축 자주 색 그대로
- **primary-soft**: `#EDE9FE` · **primary-soft-border**: `#C4B5FD`
- 구조: `<h1>` 직접 노출 (h1-row 래퍼 없음) → `<span class="hero-line">` 존재
- Pretendard · hero-line · fadeUp · `:root` 8토큰 완비
- 광고 2슬롯 (`#ad-slot` · `#ad-slot-bottom`) · adsbygoogle INS 완비
- 관련 링크: 수시·수능·방학숙제·추석 연결 (교육 생태계)
- favicon: `fill='%237C3AED'` (primary와 일치)

### 도메인 분석

대학생이 "국가장학금 신청 언제 시작?"을 검색하는 순간의 감정: **희망·준비·기대**. 수시·수능의 "긴장·집중"과 같은 학생 축이지만 감정 결은 더 가볍고 밝다. 소득분위·정책적 요소는 배경이고 전면에 오는 것은 "대학생·지원·타이밍".

### 피카소 인디고(`#4F46E5`) 제안 → 채택 불가

인디고는 "공식·법·정책·청약" 축으로 확정 배정. 국가장학금은 정책 수혜자(대학생) 시각의 도구이지 정책 행정 도구가 아니다. 교육 축(자주 계열)이 도메인 정합.

### 시안 2안

#### A안: `#7C3AED` 현행 유지 (교육 축 내 밝은 변형)

primary `#7C3AED` (밝은 바이올렛) · hover `#6D28D9` (자주)

| 토큰 | 값 |
|------|-----|
| `--primary` | `#7C3AED` |
| `--primary-hover` | `#6D28D9` |
| `--primary-soft` | `#EDE9FE` |

**대비값**: `#7C3AED` vs `#FFFFFF` ≈ 8.2:1 ✓ (AAA)

**평가**: 수시·수능(`#6D28D9`)보다 밝아 "희망·기대" 에너지 분기. 같은 자주 패밀리 안에서 감정 분화. hover에 `#6D28D9`가 있어 교육 축 연결성은 유지.

**단점**: 팔레트 관리상 자주 계열이 `#6D28D9`와 `#7C3AED` 두 값으로 분기 → 누적 팔레트 표기 복잡도 소폭 증가.

#### B안: `#6D28D9` 교육 축 통일 (권고)

primary를 `#6D28D9` (자주)로 통일. 수시·수능·방학숙제와 동일 색.

| 토큰 | 값 |
|------|-----|
| `--primary` | `#6D28D9` |
| `--primary-hover` | `#5B21B6` |
| `--primary-soft` | `#EDE9FE` |
| `--primary-soft-border` | `#C4B5FD` |

**대비값**: `#6D28D9` vs `#FFFFFF` ≈ 11.7:1 ✓ (AAA · 충분한 여유)

**평가**: 교육 축 단일화 → 브랜드 일관성 최대화. 관련 링크에 이미 수시·수능·방학숙제가 연결돼 있고 같은 색이 되면 시각 생태계 완결. 단 감정 분기 없어짐.

**달리 권고: B안.** 국가장학금은 독립 감정 분기가 필요할 만큼 차별화 포인트가 명확하지 않다. 교육 축 5중(수시·수능·방학숙제·국가장학금·다음사이클) 완성을 우선.

### 세부 이슈 — h1-row 래퍼 없음

현재: `<h1>국가장학금 신청 D-day</h1>` 직접 노출 → `<span class="hero-line">` 순서.
시리즈 다른 유틸은 `<div class="h1-row"><h1>...</h1></div>` 구조.

기능상 문제 없고 hero-line은 이미 있음. h1-row 추가 여부는 다빈치 판단 요청 (강제 통일 or 현행 유지).

---

## senior-subway-free-dday (65세 지하철 무임승차 D-day)

### 실황 확인

- **primary**: `#0369A1` (스카이블루)
- **primary-hover**: `#075985` · **primary-soft**: `#E0F2FE` · **primary-soft-border**: `#7DD3FC`
- 구조: `<div class="h1-row"><h1>...</h1></div>` → `<span class="hero-line">` (h1-row + hero-line 완비)
- Pretendard · fadeUp · `:root` 9토큰(success·success-soft 추가) 완비
- 결과 카드 2상태: `eligible`(그린 `#198754`) · `waiting`(primary 스카이블루) — 도달 후 그린 전환 설계
- 광고 2슬롯 (`#ad-slot` · `#ad-slot-bottom`) · adsbygoogle INS 완비
- favicon: `fill='%230369A1'` (primary 일치)

### 도메인 분석

이 유틸의 핵심 감정: **기대·설렘·D-day**. 사용자는 "내가 언제부터 공짜 지하철을 탈 수 있지?"를 찾는다. 지하철이라는 대중교통 인프라, 공공 서비스, 복지 혜택의 교차점.

**스카이블루 `#0369A1` 적합 근거:**
- 지하철 = 교통·공공 인프라 → 스카이블루는 전 세계 대중교통 브랜딩에서 가장 보편적 색역
- "신뢰·공식·안정" 색 → 정부 복지 혜택 안내 도구에 정합
- `--primary-soft: #E0F2FE`(하늘색 연무) 배경이 "밝고 가벼운 복지 혜택" 느낌 정확히 표현
- eligible 상태가 그린(`#198754`)으로 전환 → "대기 중(스카이블루) → 혜택 획득(그린)" 감정 흐름이 논리적

**대비값**: `#0369A1` vs `#FFFFFF` ≈ 7.3:1 ✓ (AAA)

### 평가 · 확정 권고

**현행 유지 `#0369A1` 확정 권고.** 변경 불필요.

마이클이 도메인을 정확히 읽고 스카이블루를 선택했다. eligible 상태를 그린으로 분리한 설계도 "복지 혜택 획득" 감정 전환을 잘 포착. 공통 스택(h1-row·hero-line·fadeUp·2슬롯) 이미 완비.

**팔레트 신규 편입 제안**: 스카이블루 `#0369A1` = **"교통·공공 서비스·복지 혜택"** 신규 도메인 축. 이후 노인장기요양·경로당·복지 D-day 등에 자연 연결.

---

## 다빈치 판정 요청

1. **national-scholarship-dday**: B안 `#6D28D9` 교육 축 통일 확정 (권고) or A안 `#7C3AED` 현행 유지
2. **national-scholarship-dday**: h1-row 래퍼 추가 여부 (hero-line은 이미 있음)
3. **senior-subway-free-dday**: `#0369A1` 현행 유지 확정 (이견 없음 · 재확인 판정만 필요)
4. 스카이블루 `#0369A1`의 팔레트 신규 편입 확정 ("교통·공공 서비스·복지 혜택" 축)

---

## 다빈치 판정 봉인 (2026-08-19)

**판정 4건 결착 · 반려 0 · 1회 결착.**

### 1. national-scholarship-dday → **B안 `#6D28D9` 교육 축 통일 확정** (11.7:1)

달리 근거 채택. 결정적 4축:
- **팔레트 관리 단순성**: 자주 계열이 `#7C3AED`(violet-600)와 `#6D28D9`(violet-700) 두 값으로 갈리면 향후 유틸에서 "어느 자주?" 판단 부채. 감정 분기의 이론적 이점보다 팔레트 표기 부채가 큼.
- **대비 이점**: `--primary-soft: #EDE9FE` 배경 위에서 `#6D28D9`가 `#7C3AED`보다 명도 대비 강해 배경+텍스트 조합 안정.
- **관련 링크 3/4가 교육 축**(수시·수능·방학숙제) — 클릭 전후 색 일치로 "같은 시리즈" 인식 강화.
- **감정 분기의 실증 이점 미미**: 색맹·저조도 환경에서 두 자주 계열 구분 유의미성 낮음. 브랜드 일관성 이득이 확실.

**토큰 교체 2건만**: `--primary: #6D28D9` · `--primary-hover: #5B21B6` (violet-800). `--primary-soft: #EDE9FE`·`--primary-soft-border: #C4B5FD`는 마이클 세팅 유지 (violet-100/300 계열 · `#6D28D9`와 정합).

**favicon SVG `fill='%237C3AED'` → `%236D28D9`** 교체 (primary와 일관).

**참고 기록 (팔레트 정합 교정 예약)**: 8/15 susi-dday에서 primary-soft를 `#E9D5FF`(purple-200)로 확정했는데 `#6D28D9`(violet-700)와 엄밀 정합은 `#EDE9FE`(violet-100). 두 값 다 대비 통과·인지 차이 미미하므로 소급 수정 없이 다음 자주 축 유틸부터 violet 계열(EDE9FE·C4B5FD)을 표준으로 정리.

### 2. national-scholarship-dday h1-row 래퍼 → **추가 안 함 · 현행 유지**

h1-row는 `wedding-gift-calculator`에서 우측 공유 버튼과 h1을 한 줄에 배치하기 위해 필요했던 조건부 구조. national-scholarship-dday엔 공유 버튼 없음 → h1-row는 빈 래퍼가 되어 무의미. h1-row는 "필요할 때만" 쓰는 조건부 구조지 시리즈 표준 아님. hero-line은 이미 있어 시리즈 정체성은 확보됨.

### 3. senior-subway-free-dday → **`#0369A1` 유지 확정** (7.3:1)

피카소·달리 완전 동의. 마이클이 도메인을 정확히 읽음:
- 스카이블루는 전 세계 대중교통 브랜딩의 보편 색역
- `--primary-soft: #E0F2FE`(하늘색 연무)가 "밝고 가벼운 복지 혜택" 감정 정확
- `eligible` 상태를 `--success: #198754` 그린으로 분리 전환한 설계는 **"대기(스카이블루) → 혜택 획득(그린)" 감정 여정을 색으로 완결한 뛰어난 마이크로 인터랙션**
- `--success` · `--success-soft` 토큰 확장까지 마쳐 상태 색역 완비

**토큰 변경 0건 · index.html 무수정 승인.**

### 4. 스카이블루 `#0369A1` → 팔레트 신규 편입 확정

**"교통·공공 서비스·복지 혜택" 도메인** 신규 편입. 이후 노인장기요양·경로당·복지 D-day 계열이 이 축으로 자연 연결.

---

### index.html 반영 요지

**national-scholarship-dday/index.html:**
- `:root`: `--primary: #7C3AED` → `#6D28D9` · `--primary-hover: #6D28D9` → `#5B21B6`
- favicon SVG `fill='%237C3AED'` → `%236D28D9`
- 기타 CSS 룰은 토큰 참조라 자동 반영 (`.hero-line` background · `.status-card.upcoming` border/bg · `.main-days` color · `.period-bar span` color · `.badge-upcoming` bg · `.s-upcoming` bg/color · `.income-value` color · `.step-num` bg · `.check-icon svg` stroke · `.related-links a` color/border/bg · `a` link 색 등 자동 자주 통일)
- `.status-card.open` 계열 그린(`#10b981`·`#059669`·`#065f46`·`#D1FAE5`·`#6EE7B7`)은 "신청 창 열림" 상태 색으로 primary와 무관 · 유지
- `.related-links a:hover { background: #ddd6fe }` (violet-200) 유지

**senior-subway-free-dday/index.html:**
- 변경 없음. 마이클 상태 그대로 최종 승인.

### 전수 보존 확인 (2건 공통)

- SEO 메타 · OG · Twitter · JSON-LD (`WebApplication`) · canonical
- `/shared/ads.css` 참조 · adsbygoogle INS · `#ad-slot` · `#ad-slot-bottom` 2슬롯 설계
- JS 계산 로직 (national-scholarship: SCHEDULES 8회차·활성/다음 창 탐색·D-day 계산·상태 카드 클래스 스위칭 · senior-subway: 만나이 계산·65세 도달일·2/29 윤년 처리·eligible/waiting 분기)
- DOM ID 전수 (national-scholarship: `#status-card`·`#status-label`·`#status-badge`·`#main-days`·`#days-sub`·`#period-bar`·`#schedule-table`·`#schedule-tbody` · senior-subway: `#birth-date`·`#btn-calc`·`#form-error`·`#result-card`·`#result-label`·`#result-days`·`#result-sub`·`#result-date-bar`·`#result-date`·`#result-age-note`)
- 크로스링크 (national-scholarship: 수시·수능·방학숙제·추석 4개 · senior-subway: 근로장려금·아동수당·연차·출생신고 4개)
- Cloudflare Analytics · 480px 반응형 미디어 쿼리 무손실

### 팔레트 누적 갱신 (2026-08-19)

| 톤 | 색값 | 도메인 |
|-----|------|--------|
| 자주 | `#6D28D9` | 학생·진학·준비 · 방학숙제·수시·수능·**국가장학금(신규)** |
| 인디고 | `#4F46E5` | 공식·법·정책·청약 |
| 그린 | `#198754` | 신뢰·권리·근로·근로장려금·자녀장려금·하자보수·최저임금 |
| 터쿠아즈 | `#0FADAD` | 축제·활기·기다림·크리스마스 |
| 주황 | `#EA580C` | 긴박감·예매·추석 |
| 코발트 | `#1971C2` | 절약·경제·재테크·자동차세 |
| 보라 | `#553C9A` | 성인 의례·예절·격식·경조사·축의금 |
| **스카이블루** | **`#0369A1`** | **교통·공공 서비스·복지 혜택·경로우대 지하철 (2026-08-19 신규)** |

---

**작성**: 피카소 (사원) 예비 분석 · 달리 (대리) 정리 · 2026-08-19
**판정**: 다빈치 (팀장) · 2026-08-19
**다음**: 클레버 (개발팀 검수)

---

## 클레버 검수 (2026-08-19)

### 4축 판정

| 축 | national-scholarship-dday | senior-subway-free-dday |
|-----|-----|-----|
| 정확성 | OK | OK |
| 완성도 | OK | OK |
| 원칙 | OK | OK |
| 배포 준비 | **조건부 준비** (사유: 소득분위 지원 금액 팩트 재확인) | **조건부 준비** (사유: 지역별 운영기관 사명·전화번호 팩트 재확인) |

### 수정 항목

**두 파일 무수정.** 다빈치 판정 결과가 index.html에 정확히 반영됨(national-scholarship `--primary`·`--primary-hover`·favicon 3건 교체 · senior-subway 무수정). 코드·SEO·JSON-LD·adsbygoogle·접근성 전수 통과.

### 실증 검증

- **JS 문법**: 2건 전수 `node --check` 통과 (nsc OK · ssf OK)
- **shared/ads.css 존재 확인**: 489B (`/Users/jim/projects/webutils/shared/ads.css`)
- **국가장학금 SCHEDULES 16개 날짜 요일 검증**: `date -jf` 실증 전수 **목요일** 통과 (한국장학재단 관례 정합 · 2025-11-20 ~ 2027-08-12 8회차 16날짜)
- **국가장학금 계산 로직 시뮬레이션**: 오늘(2026-08-19) 기준 activeSchedule 없음 · nextSchedule = `2027학년도 1학기 1차` · **D-92** 산출 (8/19→11/19 92일 · 8월 잔여 12일+9월 30+10월 31+11월 19 = 92 ✓)
- **senior-subway 계산 로직 시뮬레이션 6케이스 통과**:
  · 1961-08-19생(오늘 65세) → eligible ✓
  · 1961-08-20생(내일 65세) → D-1 ✓
  · 1961-08-18생(어제 65세) → eligible ✓
  · 1965-08-19생(만 61세) → D-1461 (윤년 2028 포함 4년) ✓
  · 1960-02-29생(2/29 · 65+1960=2025 비윤년) → 2/28 처리 · eligible ✓
  · 2/29 처리 로직 (m===1 && d===29 && result.getDate()!==29) 정상 동작

### 팩트 재확인 상신 항목 (마케팅팀 · 배포 전 필수)

1. **국가장학금 소득분위 8구간 지원 금액** (2026학년도 기준 명시)
   · 1구간(기초) 570 · 2구간 570 · 3구간 480 · 4구간 360 · 5구간 240 · 6구간 195 · 7구간 135 · 8구간 67.5 만원 (연 단위)
   · 한국장학재단 2026학년도 공식 발표값 대조 필요
   · 안전장치: disclaimer에 "매년 조정될 수 있습니다" 명시됨 → 잠정 상태 표기는 이미 안전화

2. **65세 지하철 무임 지역별 운영기관 사명·전화번호** (6개 지자체)
   · 서울교통공사 · 부산교통공사 · **대구도시철도** · 인천교통공사 · **광주도시철도** · 대전교통공사
   · **대구는 2023년 대구도시철도공사·대구시설공단 통합해 "대구교통공사"로 사명 변경 가능성** (재확인 필요)
   · 광주·기타 지자체 사명 최신성 재확인 필요
   · 전화번호 6건 최신성 재확인 필요
   · 안전장치: 안내문 아래 "역무실 방문 전 해당 기관 홈페이지에서 최신 절차를 확인" 문구 있음

### 이월 이슈 (누적 유지 · 이번 사이클 미해결)

1. WAGE_2027 확정값 원복 (8/17 이월)
2. Math.ceil 자정 정밀도 (누적)
3. `<link as="style">` 문법 (누적)
4. adsbygoogle inline slot 미삽입 (누적)
5. wedding-gift favicon 톤차 (8/17 이월)
6. **[신규]** senior-subway `max="2026-08-19"` 하드코딩 (JS로 오늘 날짜 동적 설정 미적용 · 실용상 무해 · 신생아가 지하철 D-day 검색할 일 없음)
7. **[신규]** 국가장학금 SCHEDULES 2028학년도 이후 미포함 (2027-08-12 이후 상태카드 "일정 종료" 표시 · 매년 갱신 필요)

### 전수 보존 확인 (2건 공통)

- SEO 메타·OG·Twitter·canonical·JSON-LD (`WebApplication`) — 다빈치 봉인과 일치
- Pretendard v1.3.9 CDN + preconnect crossorigin
- `/shared/ads.css` 참조 · adsbygoogle 2슬롯 (`#ad-slot` · `#ad-slot-bottom`) · client `ca-pub-9477150496807643` · slot 4197594404/9059038840
- DOM ID 전수 (nsc: status-card·status-label·status-badge·main-days·days-sub·period-bar·schedule-table·schedule-tbody / ssf: birth-date·btn-calc·form-error·result-card·result-label·result-days·result-sub·result-date-bar·result-date·result-age-note)
- 크로스링크 (nsc: 수시·수능·방학숙제·추석 · ssf: 근로장려금·아동수당·연차·출생신고)
- Cloudflare Analytics beacon · 480px 반응형 미디어 쿼리

### 배포 판단 상신 (대표 결정 요청 · 사마의 일일 보고 통해)

- **A안**: 두 파일 오늘 동시 배포 (disclaimer 안전장치 있음 · 팩트 재확인 후 hotfix)
- **B안**: 마케팅팀 팩트 조사(소득분위+지역별 사명·전화번호) 완료 후 두 파일 배포
- **C안**: senior-subway만 오늘 배포 (계산 로직·주 도메인 무결 · 지역별 안내는 후속 수정) · national-scholarship은 소득분위 팩트 확인 후
- **D안 (클레버 권고)**: 두 파일 모두 마케팅팀 팩트 조사 완료 후 배포. 사유:
  · 8/17 minimum-wage-2027 미확정 팩트 대기 원칙과 정합
  · 지역별 사명 오류(대구교통공사 통합 가능성)는 신뢰도 훼손 리스크 큼 (지자체 공식명은 검색 결과에서 즉시 대조됨)
  · 국가장학금 소득분위 금액은 학년도별 차이가 크고 "570만원"이 확정값인지 상한인지 애매

### 배포 준비 상태 최종

- national-scholarship-dday: **조건부 준비 · 소득분위 지원 금액 마케팅팀 팩트 확인 후 배포**
- senior-subway-free-dday: **조건부 준비 · 지역별 운영기관 사명·전화번호 마케팅팀 팩트 확인 후 배포**

`_COMMON.md §7` 준수 — `git push`·배포 실행·파일 이동 없음. 대표 결정 대기.

**검수**: 클레버 (팀장) · 2026-08-19
