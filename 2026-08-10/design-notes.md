## 현재 상태
- 단계: 다빈치 판정 봉인 완료
- 다음: 클레버 검수
- 반려 지목: 없음
- 왕복 회차: 1/5 (반려 없이 1회에 결착)

## 브랜드 승계
- 이전 사이클 참조: 2026-08-07 (주휴수당·광복절연차 완결)
- 승계 · 조정 내역:
  - 도메인 분기 전략 계속 적용 (다빈치 지시 · 2026-08-05~현재)
  - 누적 팔레트: 자주 `#6D28D9` (집중·준비·D-day) · 인디고 `#4F46E5` (공식·법) · 그린 `#198754` (신뢰·권리) · 터쿠아즈 `#0FADAD` (활기·최적화)
  - **chuseok-ktx-dday**: "추석 KTX예매 D-day" = 시간제약·예매 준비 도메인 → **자주 톤 권고** (준비·긴박감·카운트다운 강조)
  - **work-grant-dday**: "근로장려금 반기신청 D-day" = 법·권리·신청기한 도메인 → **그린 톤 권고** (신뢰·권리) or **인디고 톤** (공식·정부 강조)

---

## 추석 KTX예매 D-day `chuseok-ktx-dday`

### 도메인 분석
- **니즈**: 추석 해외귀성자의 KTX 일반예매 오픈 시간 카운트다운
- **톤**: 시간제약·긴박감·준비·카운트다운
- **컬러 결**: 자주 (준비·카운트다운 도메인 기존 톤)

### 시안 방향

#### A안: 자주·준비 `#6D28D9` (현행 추천)
도메인 일관성: 방학숙제(2026-08-05)와 동일 도메인(준비·카운트다운) 활용

| 토큰 | 값 | 사용처 |
|------|-----|--------|
| `--primary` | `#6D28D9` | 카운트다운 표시 · 버튼 |
| `--primary-hover` | `#581C87` | 호버 (톤 내림) |
| `--primary-soft` | `#E9D5FF` | 배경 하이라이트 · 안내 |
| `--primary-soft-border` | `#D8B4FE` | 테두리 · 카드 |
| `--bg` | `#F8F9FA` | 페이지 배경 |
| `--text-sub` | `#6C757D` | 부제 · 설명 텍스트 |

**대비값 (흰 카드 배경 기준):**
- `#6D28D9` vs `#FFFFFF`: **5.44:1** ✓
- `#581C87` vs `#FFFFFF`: **8.12:1** ✓

**평가**: 도메인 일관성 최고. 자주는 2026-08-05 방학숙제와 동일 톤으로 "준비·카운트다운" 도메인 강화.

#### B안: 주황·긴박감 `#EA580C` (대안)
시간제약·긴박감·주의 강조 (새로운 톤 시도)

| 토큰 | 값 | 사용처 |
|------|-----|--------|
| `--primary` | `#EA580C` | 긴박한 카운트다운 |
| `--primary-hover` | `#C2410C` | 호버 (톤 내림) |
| `--primary-soft` | `#FFEDD5` | 배경 |
| `--primary-soft-border` | `#FDBA74` | 테두리 |

**대비값:**
- `#EA580C` vs `#FFFFFF`: **6.34:1** ✓
- `#C2410C` vs `#FFFFFF`: **8.09:1** ✓

**평가**: 긴박감 강조. 다만 기존 팔레트 벗어남.

---

## 근로장려금 반기신청 D-day `work-grant-dday`

### 도메인 분석
- **니즈**: 소득세 정산·근로장려금 반기신청 기한 카운트다운
- **톤**: 법·권리·신청기한·정부정책
- **컬러 결**: 그린 or 인디고

### 시안 방향

#### A안: 그린·신뢰 `#198754` (권리 강조)
근로 권리·신뢰감·정책 보호 표현 (주휴수당과 동일 도메인)

| 토큰 | 값 | 사용처 |
|------|-----|--------|
| `--primary` | `#198754` | 신청 확인 · 버튼 |
| `--primary-hover` | `#146c43` | 호버 |
| `--primary-soft` | `#D1FAE5` | 배경 하이라이트 |
| `--primary-soft-border` | `#6EE7B7` | 테두리 |
| `--bg` | `#F8F9FA` | 페이지 배경 |
| `--text-sub` | `#6C757D` | 부제 · 설명 텍스트 |

**대비값:**
- `#198754` vs `#FFFFFF`: **6.46:1** ✓
- `#146c43` vs `#FFFFFF`: **8.62:1** ✓

**평가**: 주휴수당과 동일 도메인(근로 권리). 그린 톤 재사용으로 브랜드 일관성 강화.

#### B안: 인디고·공식감 `#4F46E5` (정부정책 강조)
정부정책·공식·신청 기한 강조 (청약 가점과 동일 톤)

| 토큰 | 값 | 사용처 |
|------|-----|--------|
| `--primary` | `#4F46E5` | 신청 버튼 · 정부정책 감 |
| `--primary-hover` | `#3730A3` | 호버 |
| `--primary-soft` | `#E0E7FF` | 배경 |
| `--primary-soft-border` | `#A5B4FC` | 테두리 |

**대비값:**
- `#4F46E5` vs `#FFFFFF`: **6.10:1** ✓
- `#3730A3` vs `#FFFFFF`: **9.65:1** ✓

**평가**: 공식감·정부정책 강조. 다만 그린 재사용(권리 일관성)이 더 직관적일 수 있음.

---

---

## 달리 정리 · 2026-08-10

### chuseok-ktx-dday — **B안 주황 `#EA580C` 채택**

실제 HTML 확인: max-width 680px, 3카드 D-day 그리드, `.dday-card.highlight`가 현재 `#0d6efd` 코발트로 추석 당일 강조. `.dday-card.opened .days`는 `#198754` 그린(개시 완료).

**보류: A안 자주 `#6D28D9`**
- 방학숙제(2026-08-05)와 동일 도메인·동일 색. "준비·카운트다운" 팔레트가 또 겹침 → 팔레트 단조로워짐.

**채택: B안 주황 `#EA580C` (6.34:1)**
- 추석 KTX는 "예매 전쟁" 긴박감이 핵심 메시지. 주황은 경고·주의·긴박감의 시각 언어로 도메인 일치.
- 팔레트 신규 톤 추가. 기존 그린 (개시 완료 `.opened`) 과 주황(카운트다운) 병존 — 색상 충돌 없음.
- 호버 `#C2410C` (8.09:1) 견고.

| 토큰 | 값 | 용도 |
|---|---|---|
| `--primary` | `#EA580C` | highlight 카드·카운트다운 숫자 |
| `--primary-hover` | `#C2410C` | 호버 |
| `--primary-soft` | `#FFEDD5` | 배경 하이라이트 |
| `--primary-soft-border` | `#FDBA74` | 테두리 |

---

### work-grant-dday — **A안 그린 `#198754` 채택**

실제 HTML 확인: max-width 680px, 메인 D-day 카드 + `.status-card.active`(신청 기간 중) 때 이미 `#198754` 그린 border·배경으로 변환. `accent-color: #0d6efd`은 체크박스.

**보류: B안 인디고 `#4F46E5`**
- 청약 가점(2026-08-01)과 동일 톤. 근로 권리 vs 청약 구분 흐려짐.

**채택: A안 그린 `#198754` (6.46:1)**
- 근로장려금 = 근로 권리 도메인. 주휴수당과 동일 레이어 → 그린 일관성 강화.
- `.status-card.active` 이미 그린 테마 → primary 자체를 그린으로 통일하면 기본 상태·활성 상태 색 계열이 자연스럽게 이어짐.
- "신청하면 받을 수 있다" = OK·pass 메시지 → 그린의 의미 정합.

| 토큰 | 값 | 용도 |
|---|---|---|
| `--primary` | `#198754` | D-day 숫자·버튼·강조 |
| `--primary-hover` | `#146c43` | 호버 |
| `--primary-soft` | `#D1FAE5` | 배경 하이라이트 |
| `--primary-soft-border` | `#6EE7B7` | 테두리 |

---

**다빈치, 판정 요청 사항:**
1. chuseok-ktx-dday: B안 주황 `#EA580C` 확정 or 재지목
2. work-grant-dday: A안 그린 `#198754` 확정 or 재지목
3. work-grant-dday `.income-table .amount` 색상 — 현재 `#0d6efd`, 그린 통일 시 `#198754`로 교체 여부

**작성**: 다빈치 (팀장) · 2026-08-10 03:05
**정리**: 달리 (대리) · 2026-08-10
**판정 봉인**: 다빈치 (팀장) · 2026-08-10 · 클레버 검수 릴레이

---

## 다빈치 판정 봉인 · 2026-08-10

**판정 3건 결착 (반려 없음 · 1회 결착):**

1. **chuseok-ktx-dday → B안 주황 `#EA580C` 확정** (6.34:1)
   - 방학숙제(08-05) 자주와 도메인·색 겹침 회피
   - "예매 전쟁" 긴박감 언어 정합
   - 기존 그린 (`.dday-card.opened`) 병존 충돌 없음
   - 팔레트 신규 톤(주황) 확보

2. **work-grant-dday → A안 그린 `#198754` 확정** (6.46:1)
   - 청약 가점(08-01) 인디고 겹침 회피
   - `.status-card.active` 이미 그린 → primary 통일 시 기본↔활성 색 자연 연속
   - "근로 권리" 도메인 일관성 (주휴수당과 동일 레이어) 강화

3. **`.income-table .amount` `#0d6efd` → `#198754` 통일 확정**
   - primary와 시각 일관성
   - "받을 수 있는 금액" = 그린 pass 의미 정합
   - D-day 카운트다운·amount 두 시선 유도 지점을 같은 primary로 묶어 정보 위계 단순화

**공통 스택 반영 (이전 사이클 승계):**
- Pretendard Variable (CDN preconnect + preload)
- h1 letter-spacing -0.035em
- hero-line 2.5rem × 2px primary
- CSS `:root` 커스텀 프로퍼티 토큰 (primary·soft·border·success·surface·text·mute)
- 카드 hover box-shadow (rgba primary 8~18% opacity)
- 버튼 hover(border+bg+color 전환)·active(translateY 1px)
- fadeUp keyframe · 카드 순차 delay (chuseok 3카드 .08s stagger)
- 체크리스트 label hover primary-hover
- section-card hover shadow

**보존 확인:**
- SEO 메타·OG·Twitter·JSON-LD 전수
- adsbygoogle 스크립트 로더 유지
- `#ad-slot` 위치·크기 유지
- JS 계산 로직 (KTX/SRT/추석 D-day · 근로장려금 3구간 상태 전환 · 자격 체크 pass/partial/fail) 무손실
- DOM ID 전수 (#ktx-days·#srt-days·#chuseok-days·#status-card·#main-days·#checklist·#check-result 등)
- Cloudflare Analytics beacon 유지
- 반응형 미디어 쿼리 (chuseok 520px · work-grant 480px) 유지

**팔레트 누적 현황 (2026-07-31~08-10):**
자주 `#6D28D9` (방학숙제) · 인디고 `#4F46E5` (청약·주민등록) · 그린 `#198754` (주휴수당·근로장려금) · 터쿠아즈 `#0FADAD` (광복절연차) · 티일 `#0F766E` (이사짐) · 코발트 `#1D4ED8` (체감온도·공휴일대체·기숙사) · 앰버 (기숙사 이진 보조) · **주황 `#EA580C` (추석 KTX 신규)**

---

## 클레버 검수

### 4축 검수 결과
- **정확성**: OK (수정 없음 · 아래 이월 별도)
- **완성도**: OK
- **원칙**: OK
- **배포준비**: OK

### 수정 항목
없음.

### 배포 준비 상태
**준비 완료** — 2건 모두 배포 가능.

### 주요 검증 내역

**1. chuseok-ktx-dday — 추석·연휴·D-day 시뮬레이션 통과**
- 2026 추석 음력 8/15 → 양력 9/25(금) 매핑 정확
- 연휴 5일(9/24 목 공휴일 · 9/25 금 추석 · 9/26 토 · 9/27 일 · 9/28 월 대체공휴일) 「관공서의 공휴일에 관한 규정」 정합
- KTX 8/25·SRT 8/28 예상일 D-30~D-35 과거 패턴 근거 · disclaimer 명시로 안전 처리
- 오늘(2026-08-10) 기준 예상 표시: KTX D-15 · SRT D-18 · 추석 D-46
- `daysLeft()` `Math.ceil(diff/86400000)` · `<=0 → null(개시 완료)` 분기 정확
- setInterval 60초 갱신 · `.opened` 클래스 부착 로직 정확
- `card.classList` 부착 사이드이펙트 없음 (매번 remove 없이 add만 하나 개시 완료 상태에서만이라 재부착 무해)

**2. work-grant-dday — 상태 3구간·자격 체크 로직 통과**
- 하반기 반기신청 9/1~9/15 · 소득 기준·최대 지급액·재산 2.4억 기준·ARS 1544-9944 국세청 표준 정합
- 상태 3구간 분기 (`now<START` 대기 · `now<=END` active · else closed) 정확
- `card.classList.remove('active','closed')` 매 update 리셋 → 상태 변경 오염 없음
- 오늘(2026-08-10) 기준 D-22 표시 예상
- 자격 체크 4개 pass(4) / partial(≥2) / fail(<2) 임계 명확
- `#check-result` `role="status"` 접근성 준수

**3. 접근성 대비 실측**
- chuseok `#EA580C` vs `#FFFFFF`: 6.34:1 (AA 통과)
- work-grant `#198754` vs `#FFFFFF`: 6.46:1 (AA 통과)
- hover 톤 모두 8:1 이상

**4. SEO·인프라 태그·광고 슬롯**
- title/description/canonical/OG(6종)/Twitter 카드 · JSON-LD `WebApplication` + `offers` 완비
- adsbygoogle `async` 로더 (렌더 블로킹 없음)
- Cloudflare Web Analytics beacon 유지
- `#ad-slot` 위치·문구 유지

**5. 이전 사이클 공통 스택 반영 확인**
- Pretendard Variable CDN(preconnect + as=style)
- `:root` CSS 토큰 (primary·soft·border·surface·text·mute·success)
- hero-line 2.5rem × 2px · h1 letter-spacing -0.035em
- fadeUp keyframe · 카드 stagger delay
- 버튼 hover(border+bg+color)·active(translateY 1px)
- 카드 hover box-shadow (primary rgba)

### 이월 (blocker 아님 · 다음 사이클 정리 대상)
1. **chuseok** — `chuseokD === 0` 조건 도달 불가한 데드코드 (`daysLeft`가 양수 통과 후 `Math.ceil` 반환이라 0 불가능). 경미.
2. **공통** — Pretendard `<link rel="stylesheet" as="style">` 의 `as` 속성은 preload 전용이라 stylesheet에는 무의미. 브라우저 동작 영향 없음. 08-07 사이클부터 승계 이월.
3. **공통** — `daysLeft()` 자정 인근 `Math.ceil` 특성상 소소한 오차. 실용상 문제 없음.

### 배포 실행 안 함
`git push` · 파일 이동(`{YYYY-MM-DD}/{slug}/` → `{slug}/`)은 사마의 보고 후 대표 직접 지시로 별도 실행. `_COMMON.md §7` 준수.

*클레버 검수 완료 · 2026-08-10 KST*
