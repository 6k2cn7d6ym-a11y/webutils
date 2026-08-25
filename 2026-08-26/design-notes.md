## 현재 상태
- 단계: 다빈치 판정 봉인 (완료)
- 다음: — (클레버 검수)
- 반려 지목: 없음 (1회차 결착)
- 왕복 회차: 1/5

## 브랜드 승계
- 이전 사이클 참조: 2026-08-22/design-notes.md (basic-pension-dday · year-end-tax-preview-dday)
- 승계 내역: 팔레트 11축 봉인 그대로 · Pretendard Variable · hero-line · fadeUp · 광고 2슬롯 구조

| 톤 | 색값 | 도메인 |
|----|------|--------|
| 자주 | `#6D28D9` | 학생·진학·준비 |
| 인디고 | `#4F46E5` | 공식·법·정책·청약 |
| 그린 | `#198754` | 신뢰·권리·근로·자녀장려금 |
| 터쿠아즈 | `#0FADAD` | 축제·활기·기다림 |
| 주황 | `#EA580C` | 긴박감·예매 |
| 코발트 | `#1971C2` | 절약·경제·재테크 |
| 보라 | `#553C9A` | 성인 의례·경조사·축의금 |
| 스카이블루 | `#0369A1` | 교통·공공 서비스·복지 혜택·기초연금 |
| amber | `#B45309` | 부동산·주거·계약·임대차 |
| teal | `#0F766E` | 의료·요양·노인장기요양보험 |
| blue | `#1D4ED8` | 세무·연말정산·환급 |

---

## birth-registration-dday (출생신고 D-day)

### 실황 확인

| 토큰 | 마이클 값 | 비고 |
|------|-----------|------|
| `--primary` | `#0369A1` (sky-700) | 스카이블루 축 |
| `--primary-hover` | `#075985` (sky-800) | |
| `--primary-soft` | `#F0F9FF` (sky-50) | basic-pension과 동일 |
| `--primary-soft-border` | `#BAE6FD` (sky-200) | |
| `--warn` | `#D97706` (amber-600) | 과태료 경고 · 오늘 마감 상태 |
| `--danger` | `#b91c1c` | 기한 초과 상태 |
| favicon | 👶 | 출생·신생아 도메인 정합 ✓ |

구조: h1 직접 노출 · hero-line ✓ · 광고 2슬롯 ✓ · SEO·JSON-LD·CF Analytics 완비 ✓
3상태: ok(sky soft D-[n]) · today(warn amber 오늘 마감) · over(danger 기한 경과)

### 도메인 분석

출생신고를 찾는 사용자: 신생아를 출산한 지 얼마 안 된 부모. "출생신고 언제까지야?"

감정 톤: **기쁨 + 가벼운 긴장** — 기한 내 처리하면 별문제 없음. notice-box warn(amber)은 과태료 5만원 경고. 스트레스 낮음, positive 상황.

**스카이블루 적합성:**
기존 축(senior-subway·basic-pension)은 "정부 복지 혜택 수령" 맥락. 출생신고는 "정부 행정 의무 이행" 맥락으로 결이 약간 다르지만, 둘 다 "공공 행정 서비스" 상위 카테고리 안에 있음. 출생신고 → 주민센터 방문 → 공공 행정 신고 절차 확장에 무리 없음. 신생아 탄생 맥락(기쁨·안도)에 sky blue의 밝고 온화한 색감이 정합.

### 색 판단

**스카이블루 `#0369A1` 현행 유지 권고.**
- 대비 ≈ 6.0:1 AA ✓
- 👶 favicon 도메인 정합 ✓ — 변경 불필요
- soft `#F0F9FF`/`#BAE6FD`: basic-pension과 동일값 · 유지 권고

---

## inheritance-waiver-dday (상속포기 신청 D-day)

### 실황 확인

| 토큰 | 마이클 값 | 비고 |
|------|-----------|------|
| `--primary` | `#0369A1` (sky-700) | birth-registration과 동일 |
| `--primary-hover` | `#075985` | |
| `--primary-soft` | `#F0F9FF` (sky-50) | |
| `--primary-soft-border` | `#BAE6FD` (sky-200) | |
| `--warn` | `#D97706` | D-7 이내 임박 상태 |
| `--danger` | `#b91c1c` | 기한 초과 상태 |
| favicon | ⚖ | 법원·사법 도메인 정합 ✓ |

구조: h1 직접 노출 · hero-line ✓ · 광고 2슬롯 ✓ · SEO·JSON-LD·CF Analytics 완비 ✓
4상태: ok(sky soft D-7 초과) · warn(amber D-7 이내 임박) · D-0(warn) · over(danger 기한 경과)

### 도메인 분석

상속포기를 찾는 사용자: 가족이 사망한 직후 빚이 있음을 알게 된 상속인. "상속포기 언제까지야, 빚 다 물어야 하나?"

감정 톤: **무겁고 긴박함**. 기한 초과 시 결과가 치명적(빚 전액 상속). notice-box가 `--danger`(red) 처리된 이유.

**스카이블루 적합성 문제:**

스카이블루 현행 축 사용 유틸: senior-subway(교통·복지), basic-pension(노인 연금), birth-registration(출생 신고). 셋 모두 **positive 또는 중립 행정 절차**.

상속포기는 질적으로 다름:
- 사망(grief) + 부채 위기 + **가정법원 민사 신청** — 주민센터 민원 아님
- 빚 상속 위험 = 고부담·고긴장
- sky soft(`#F0F9FF`) result card ok 상태: "D-87 여유있음"에 너무 밝고 온화한 배경 — 긴박함 전달 부족

스카이블루의 "복지·교통·신생아" 색감이 이 유틸의 감정 톤(사망·부채·법원)과 불일치.

### 시안

**A안: `#0369A1` 스카이블루 현행 유지**
- 장점: 변경 없음. "공공·법적 절차" 광의 묶기.
- 단점: 도메인 감정 톤 불일치 (복지/교통/출생 vs 사망/부채/법원).

**B안: `#4F46E5` 인디고 변경 — 달리 권고**
- 기존 인디고 축: "공식·법·정책·청약" — **가정법원 민사 신청 귀속에 가장 자연스러움**
- 대비 ≈ 6.1:1 AA ✓
- 연동 수정 토큰: primary-soft `#EEF2FF`(indigo-50) · primary-soft-border `#C7D2FE`(indigo-200) · primary-hover `#4338CA`(indigo-800)
- 인디고의 "공식·엄격·법적 절차" 색감 → 가정법원 신청 문서 작업에 부합
- 기존 인디고 유틸(청약 등)과 공통 패턴: "국가 기관을 통한 법적 신청"
- 팔레트 12축 확장 없이 기존 축 심화 (11축 유지 ✓)

**C안: 신규 색 (법원·상속·민사 전용)**
- 단점: 단일 유틸로 12번째 축 개설 → 과도. 불채택.

---

## 다빈치 판정 요청 (3건)

**birth-registration-dday:**

1. **primary `#0369A1` 스카이블루** — 현행 유지 권고. 공공 행정 신고 축 확장 적합. 재확인 판정만.

**inheritance-waiver-dday:**

2. **primary 색 선택** — **B안 `#4F46E5` 인디고** (기존 "공식·법·정책" 축 귀속 · 대비 6.1:1 AA) vs A안 `#0369A1` 스카이블루 현행 유지. **달리 B안 권고.**

3. **B안 채택 시 연동 수정** — `:root` 수정 3토큰 (primary `#4F46E5` · primary-hover `#4338CA` · primary-soft `#EEF2FF` · primary-soft-border `#C7D2FE`) · compare-table th 배경색 연동. 나머지(warn/danger/success 상태 색) 무수정.

---

**작성**: 달리 (대리) 단독 처리 · 피카소 시안 미작성으로 달리가 도메인 분석·색 판단까지 수행 · 2026-08-26
**판정 대기**: 다빈치 (팀장)

---

## 다빈치 판정 봉인 (2026-08-26)

**판정 3건 1회 결착 · index.html 반영 1건(4토큰+favicon fill)·1건 무수정.**

**birth-registration-dday**

1. **primary `#0369A1` 스카이블루** — 현행 유지 **승인**. 무수정. 스카이블루 축이 "공공 행정 서비스" 상위 카테고리로 자연 확장. 감정 톤(기쁨·안도) + 색감(밝고 온화) 정합. 👶 favicon 유지. soft 토큰 basic-pension과 동일값 유지 — 노인·복지 축과 신생아 축이 같은 sky-50/sky-200 세팅 쓰는 이유는 둘 다 "안심되는 대기 상태" 정서이기 때문. 통일 정당. 스카이블루 축 4중 완성(경로우대·기초연금·출생신고 + 잠재).

**inheritance-waiver-dday**

2. **primary — B안 `#4F46E5` 인디고 채택**. 달리 대리 도메인 분석 정확 · A안 기각. 채택 근거(달리 근거 위에 얹음):
   - **감정 톤 논리**: 스카이블루 축 3중(교통 혜택 수령·연금 수령·출생 신고)의 공통 정서는 "정부로부터 무언가 받거나 기록하는 절차"(수혜/등록). 상속포기는 "정부(법원)에 부담을 벗어달라 신청"(방어/회피)로 벡터 반대. 색 축 오염 위험.
   - **시각 앵커링**: 인디고 축의 기존 유틸(주택청약 등)이 이미 "국가 기관 신청 서식"의 색 코드를 확립. 가정법원 신청은 같은 스키마.
   - **접근성**: 대비 6.1:1 AA 안전 · 스카이블루 6.0:1과 대등.
   - **팔레트 유지**: 12축 확장 없음 · 인디고 축 심화(청약·상속포기)로 축 정체성 강화.

3. **B안 연동 수정 4토큰** — 승인·전건 반영:
   - `--primary #0369A1 → #4F46E5` (indigo-600)
   - `--primary-hover #075985 → #4338CA` (indigo-800)
   - `--primary-soft #F0F9FF → #EEF2FF` (indigo-50)
   - `--primary-soft-border #BAE6FD → #C7D2FE` (indigo-200)
   - favicon SVG rect fill `%230369A1 → %234F46E5` (파비콘 배경도 축 정합 위해 연동 · ⚖ 이모지 유지)
   - `.compare-table th` 배경은 `var(--primary-soft)`·`var(--primary-hover)` 참조로 자동 연동 (직접 색값 없음 · 무수정)
   - warn/danger/success 3상태 색 무수정 (기한 임박/초과 신호는 축과 독립 · 마이클 세팅 유지)

**반영 내역**

- `inheritance-waiver-dday/index.html` line 35~38 — `:root` 4토큰 교체
- `inheritance-waiver-dday/index.html` line 17 — favicon rect fill 인디고 연동
- `birth-registration-dday/index.html` — **무수정 최종 승인**

**팔레트 누적 (2026-08-26 확정 · 11축 유지 · 축 심화):**
- 스카이블루 `#0369A1`: 교통·공공 서비스·복지 혜택·경로우대 지하철·기초연금·**출생신고(신규)** — 축 4중
- 인디고 `#4F46E5`: 공식·법·정책·청약·**상속포기 가정법원 신청(신규)** — 국가 기관 신청 서식 축 심화

**축 사용 원칙 명시 (신규 봉인):**
- 스카이블루 = "정부로부터 수혜·등록"(수혜/기록 벡터)
- 인디고 = "정부·법원에 신청·청구"(신청/청구 벡터)
- 두 축의 감정·행위 벡터 구분 확정. 향후 공공 도메인 유틸은 이 기준으로 자동 분기.

**교정 예약 유지:**
- 자주 축 violet soft 표준화(2026-08-19)
- long-term-care done CSS 토큰 리팩터(2026-08-21)

**봉인**: 다빈치 · 2026-08-26 03:20 KST

---

## 클레버 검수 (2026-08-26)

### birth-registration-dday

- 4축 검수 결과: [정확성: OK / 완성도: OK / 원칙: OK / 배포준비: OK]
- 수정 항목: 없음
- 배포 준비 상태: 준비 완료

**정확성 실증:**
- `addOneMonth()` 시뮬 5케이스 전수 통과
  - 출생일 2026-07-27 + 1개월 = 2026-08-27 (오늘 2026-08-26 기준 D-1 · ok)
  - 출생일 2026-07-26 + 1개월 = 2026-08-26 (오늘 D-0 · today 카드)
  - 출생일 2026-07-25 + 1개월 = 2026-08-25 (오늘 D-1일 경과 · over 카드)
  - 월경계 1월 31일 + 1개월 = 2월 28/29일 (Math.min lastDay clamp 정상)
  - 12월 31일 + 1개월 = 1월 31일 (targetY++ 정상 · 연 경계 처리)
- 미래 출생일 방지 · NaN 체크 · 빈 입력 방지 3중 가드 정상

**완성도 실증:**
- 다빈치 판정 무수정 반영 정확 (favicon 👶 line 17 · primary #0369A1 line 35 · hover #075985 line 36 · soft #F0F9FF line 37 · soft-border #BAE6FD line 38)
- notice-box amber `--warn-soft`/`--warn-border` 과태료 경고 톤 정합
- 3상태(ok/today/over) 색 분기 시각 정상

**원칙 실증:**
- SEO 태그 완비 (title/description/og·twitter/canonical) · JSON-LD WebApplication 온전
- 대비: primary #0369A1 흰색 배경 ≈ 6.0:1 AA ✓
- 시맨틱 태그(main/nav/h1/h2/footer) · role="alert"·aria-live 접근성 ✓
- 광고 슬롯 2개(id="ad-slot"·id="ad-slot-bottom") 유지 · adsbygoogle.push 2회 호출 정상
- CF Analytics beacon.min.js token 정상 삽입
- 480px 반응형 브레이크포인트 완비

**배포 준비 실증:**
- 외부 의존 3종(Pretendard CDN · adsbygoogle · CF Analytics) — 표준 세팅
- 관련 링크 `/child-care-grant-dday/`·`/work-grant-dday/` 이전 배포분 링크
- footer 경로 `/privacy` · `/contact.html` — 이전 사이클(basic-pension·senior-subway-free) 관례 승계 확인

---

### inheritance-waiver-dday

- 4축 검수 결과: [정확성: OK / 완성도: 수정 1건 / 원칙: OK / 배포준비: OK]
- 수정 항목:
  · `.related-links a:hover` 배경 `#E0F2FE`(sky-100) → `#E0E7FF`(indigo-100) · 마이클이 birth-registration에서 CSS 카피한 후 primary 축을 인디고로 변경했으나 hover 하드코드는 스카이 잔존 · 다빈치 판정은 4토큰 + favicon fill + compare-table th 자동연동만 명시했고 이 위치 놓침 · 축 정합 회복
- 배포 준비 상태: 준비 완료

**정확성 실증:**
- `addMonths(date, 3)` 시뮬 6케이스 전수 통과
  - 상속개시 2026-06-26 + 3개월 = 2026-09-26 (오늘 2026-08-26 기준 D-31 · ok)
  - 5월 31일 + 3개월 = 8월 31일 (lastDay=31 clamp)
  - 11월 30일 + 3개월 = 2027-02-28 (targetM=13·targetY++·lastDay=28 clamp)
  - 12월 31일 + 3개월 = 2027-03-31 (연 경계·lastDay=31 clamp)
  - D-8·D-7·D-0·D--1 4상태 분기 실증(ok/warn/warn/over) · D-7 이내 임박 로직 정상
- 미래 상속개시일 방지 · NaN 체크 · 빈 입력 방지 3중 가드 정상

**완성도 실증:**
- 다빈치 판정 4토큰 + favicon fill 정확 반영 (primary #4F46E5 line 35 · hover #4338CA line 36 · soft #EEF2FF line 37 · soft-border #C7D2FE line 38 · favicon rect fill %234F46E5 line 17 · ⚖ 이모지 유지)
- compare-table th `background: var(--primary-soft)` · `color: var(--primary-hover)` 자동 연동 정상
- notice-box `--danger-soft`/`--danger-border` — 도메인 정합(사망·부채·법원 무거운 톤)
- 4상태(ok/warn D-7 이내/warn D-0/over) 색 분기 정상
- 클레버 수정 후 hover 배경 indigo-100 정합 (축 오염 제거)

**원칙 실증:**
- SEO 완비 · JSON-LD 온전
- 대비: primary #4F46E5 흰색 배경 ≈ 6.1:1 AA ✓
- 시맨틱 태그 · role="note"/role="alert" · aria-live 접근성 ✓
- 광고 슬롯 2개 유지 · CF Analytics 삽입 정상
- 480px 반응형 브레이크포인트 완비 (compare-table 12px 축소 포함)

**배포 준비 실증:**
- 외부 의존 표준 3종
- 관련 링크 `/funeral-condolence-calculator/`·`/long-term-care-dday/` — long-term-care는 이전 사이클 배포분
- footer 경로 관례 승계

---

**클레버 총평:**
- 두 파일 모두 배포 준비 완료 (birth-registration 무수정 · inheritance-waiver 축 오염 hover 1건 수정)
- 다빈치 판정은 :root 토큰·favicon·compare-table 계열 축 전환은 정확했으나 `.related-links a:hover` 잔존 하드코드는 놓침 · 클레버 검수에서 캐치
- 팩트 재확인 상신 0건 (기한 계산 관용 로직 정합 · disclaimer로 실무 확인 안내 완비 · 민법 제155조·157조 초일 불산입 관례는 안내 목적 서비스에서 관용 계산 유지 정당)
- 마이클 코드 품질 4축 총평: **가드·시맨틱·SEO·JSON-LD·CF Analytics 세팅 재사용성 높음 · 축 전환 시 하드코드 잔재 sweep 절차 추가 권고(다음 사이클 개발팀 라인)**
- 배포 실행·파일 이동 없음 (`_COMMON.md §7` 준수 · 대표 지시 대기)

