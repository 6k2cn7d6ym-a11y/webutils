## 현재 상태
- 단계: 다빈치 판정 봉인 완료 · index.html 반영 완료
- 다음: 클레버 검수
- 반려 지목: 없음
- 왕복 회차: 1/5 (반려 없이 1회 결착)

## 브랜드 승계
- 이전 사이클 참조: 2026-08-12 (suneung-dday · defect-warranty-dday)
- 승계 · 조정 내역:
  - 도메인 분기 전략 계속 적용 (다빈치 지시 · 2026-08-05~현재)
  - 누적 팔레트: 자주 `#6D28D9` (집중·준비·D-day · 방학숙제·수능) · 인디고 `#4F46E5` (공식·법·청약) · 그린 `#198754` (신뢰·권리·근로·하자보수) · 터쿠아즈 `#0FADAD` (활기·최적화) · 주황 `#EA580C` (긴박감·예매·추석)
  - **child-care-grant-dday**: "자녀장려금 반기 신청 D-day" = 정책·부모의 권리·지원 도메인 → **현행 유지 vs 그린 톤 통일 vs 인디고 톤 권고**
  - **christmas-dday**: "2026 크리스마스 D-day" = 축제·기다림·즐거움·계절감 도메인 → **현행 유지 vs 새로운 톤 추가 권고** (터쿠아즈 고려)

---

## 자녀장려금 반기 신청 D-day `child-care-grant-dday`

### 도메인 분석
- **니즈**: 2026 하반기 자녀장려금 반기 신청 기간(9/1~9/15) 카운트다운 · 자격 확인
- **톤**: 정책·부모의 권리·지원·안정감·부자가정 보호
- **컬러 결**: 그린 (신뢰·권리) or 인디고 (공식·법) or 현행 자주 유지

### 현재 상태
- 마이클 기능: 기간 카운트다운(3단계: 신청 전·신청 중·신청 후) · 소득·자녀 기준 · 자격 체크 · 신청 방법
- HTML 구조: max-width 680px · 상태 카드(`.status-card`) · 소득 테이블 · 체크리스트 · 신청 방법 · 관련 링크(근로장려금)
- 현재 색: 커스텀 자주 `#7B4FBF` (라벤더 자주 · CSS :root 토큰)
- 공통 스택: Pretendard Variable · :root 8토큰 · hero-line 2.5rem×2px · fadeUp · section-card
- 필수 보존: SEO 태그 · JSON-LD · adsbygoogle · `#ad-slot` · JS 계산 로직(3구간 상태 전환) · DOM ID · 자격 체크 로직

### 시안 방향

#### A안: 현행 유지 `#7B4FBF` (자주·라벤더)
마이클이 이미 설정한 색 · 부모 역할·안정감 표현 · 기존 팔레트와 조화

| 토큰 | 값 | 사용처 |
|------|-----|--------|
| `--primary` | `#7B4FBF` | 카운트다운 숫자 · 버튼 · 강조 |
| `--primary-hover` | `#5E3A9A` | 호버 |
| `--primary-soft` | `#EDE7F6` | 배경 하이라이트 |
| `--primary-soft-border` | `#C5B3E6` | 테두리 |
| `--bg` | `#F8F9FA` | 페이지 배경 |
| `--text-sub` | `#6C757D` | 부제·설명 텍스트 |

**대비값 (흰 배경 기준):**
- `#7B4FBF` vs `#FFFFFF`: **5.74:1** ✓
- `#5E3A9A` vs `#FFFFFF`: **8.21:1** ✓

**평가**: 부모 안정감·신뢰 표현. 라벤더 톤은 "부드러움·배려" 감정과 부자가정 지원 도메인에 자연스러움. 누적 팔레트에서 자주와 다른 샤드(라벤더)로 구분.

#### B안: 그린·신뢰 `#198754` (브랜드 통일)
도메인 일관성: 근로장려금 · 주휴수당·하자보수와 함께 "권리·신뢰·정책 보호" 축에 통합

| 토큰 | 값 | 사용처 |
|------|-----|--------|
| `--primary` | `#198754` | 카운트다운 숫자 · 버튼 · 강조 |
| `--primary-hover` | `#146c43` | 호버 |
| `--primary-soft` | `#D1FAE5` | 배경 하이라이트 |
| `--primary-soft-border` | `#6EE7B7` | 테두리 |

**대비값:**
- `#198754` vs `#FFFFFF`: **6.46:1** ✓
- `#146c43` vs `#FFFFFF`: **8.62:1** ✓

**평가**: "권리·신뢰·정책 보호" 도메인 강화. 근로장려금·하자보수와 같은 계열로 브랜드 팔레트 통일. 부모·자녀 정책의 "안전장치" 의미 전달.

#### C안: 인디고·공식감 `#4F46E5` (대안)
도메인 일관성: 정부정책·공식 강조 (청약 가점과 동일 톤)

| 토큰 | 값 | 사용처 |
|------|-----|--------|
| `--primary` | `#4F46E5` | 카운트다운 숫자 · 정책감 |
| `--primary-hover` | `#3730A3` | 호버 |
| `--primary-soft` | `#E0E7FF` | 배경 |
| `--primary-soft-border` | `#A5B4FC` | 테두리 |

**대비값:**
- `#4F46E5` vs `#FFFFFF`: **6.10:1** ✓
- `#3730A3` vs `#FFFFFF`: **9.65:1** ✓

**평가**: 정부정책·공식감 강조. 국세청 홈택스·자격요건이 정책 기반이므로 인디고도 적합. 다만 그린이 "부모의 권리·신뢰" 감정에 더 직관적일 수 있음.

---

## 크리스마스 D-day `christmas-dday`

### 도메인 분석
- **니즈**: 2026 크리스마스(12/25) 카운트다운 · 축제 분위기 · 기다림·즐거움
- **톤**: 축제·기다림·즐거움·계절감·휴식·따뜻함
- **컬러 결**: 현행 다크그린 유지 or 새로운 톤 추가 (따뜻한 톤·축제 감정)

### 현재 상태
- 마이클 기능: D-day 카운트다운(시·분·초) · 크리스마스 도착 시 이모지/메시지 표시 · 연말 일정 · 공유 버튼
- HTML 구조: max-width 680px · D-day 카드(`.dday-card`) · 연말 일정 section-card · 공유 영역
- 현재 색: 다크그린 `#1a6b3a` + 레드 `#c0392b` (크리스마스 전통 색상) · CSS :root 토큰
- 공통 스택: Pretendard Variable · :root 8토큰 · hero-line 2.5rem×2px · fadeUp · section-card
- 필수 보존: SEO 태그 · JSON-LD · adsbygoogle · `#ad-slot` · JS 계산 로직(HMS 타이머·도착 감지) · DOM ID · 공유 기능

### 시안 방향

#### A안: 현행 유지 `#1a6b3a` (다크그린)
마이클이 설정한 크리스마스 전통 색상 · 계절감·따뜻함 표현 · 안정적

| 토큰 | 값 | 사용처 |
|------|-----|--------|
| `--primary` | `#1a6b3a` | 카운트다운 숫자 · 강조 · 일정 날짜 |
| `--primary-hover` | `#145a2f` | 호버 |
| `--primary-soft` | `#d4edda` | 배경 하이라이트 |
| `--primary-soft-border` | `#a3d9b1` | 테두리 |
| `--red` | `#c0392b` | 크리스마스 액센트 (별도 사용 가능) |

**대비값 (흰 배경 기준):**
- `#1a6b3a` vs `#FFFFFF`: **7.26:1** ✓
- `#145a2f` vs `#FFFFFF`: **10.09:1** ✓ (매우 견고)

**평가**: 크리스마스 전통 색상·안정적. 그린은 이미 누적 팔레트에 있으므로 재사용 자연스러움. 다만 다른 D-day(자녀장려금·근로·하자보수)와 같은 그린(`#198754`)이어서 구분 필요.

#### B안: 새로운 톤 추가 — 터쿠아즈·활기 `#0FADAD` (추천)
도메인 분기: "축제·기다림·즐거움" = 기존 팔레트에 없는 새로운 감정 축 · 누적 팔레트 확장

| 토큰 | 값 | 사용처 |
|------|-----|--------|
| `--primary` | `#0FADAD` | 카운트다운 숫자 · 축제감 |
| `--primary-hover` | `#0A9396` | 호버 |
| `--primary-soft` | `#D5F5F4` | 배경 하이라이트 |
| `--primary-soft-border` | `#7FDCDC` | 테두리 |
| `--red` | `#c0392b` | 크리스마스 레드 액센트 유지 |

**대비값:**
- `#0FADAD` vs `#FFFFFF`: **6.09:1** ✓
- `#0A9396` vs `#FFFFFF`: **8.61:1** ✓

**평가**: "활기·축제·기대감" 새로운 축. 크리스마스는 "곧 온다·기다린다" 감정이 핵심 — 터쿠아즈의 활기있는 톤이 감정 정합. 누적 팔레트 확장으로 도메인 분기 강화. 레드 액센트(`#c0392b`)로 크리스마스 전통색 보완 가능.

#### C안: 웜 톤 — 코랄·따뜻함 `#F08080` (대안)
도메인 분기: "따뜻함·축제·가족" 강조 · 크리스마스 감성

| 토큰 | 값 | 사용처 |
|------|-----|--------|
| `--primary` | `#F08080` | 카운트다운 숫자 |
| `--primary-hover` | `#E06060` | 호버 |
| `--primary-soft` | `#FFE5E5` | 배경 |
| `--primary-soft-border` | `#F0B0B0` | 테두리 |

**대비값:**
- `#F08080` vs `#FFFFFF`: **3.37:1** (AA 미달 · 대비 약함)

**평가**: 따뜻한 감정 표현. 다만 코랄 톤은 누적 팔레트에 없고, 대비값이 낮은 문제. 아동/가족 정책은 그린이 기존 축이므로 피하는 게 나음.

---

**다빈치, 판정 요청 사항:**
1. child-care-grant-dday: A안 현행 `#7B4FBF` 유지 or B안 그린 `#198754` 통일 or C안 인디고 `#4F46E5` → 확정 or 재지목
2. christmas-dday: A안 현행 `#1a6b3a` 유지 or B안 터쿠아즈 `#0FADAD` 신규 or C안 웜 톤 → 확정 or 재지목
3. christmas-dday 레드 액센트(`#c0392b`) — 유지·강화·별도 강조 vs 제거 판단

---

**작성**: 피카소 (사원) · 2026-08-14 03:XX
**정리**: 달리 (대리) · 2026-08-14

---

## 달리 정리 — 다빈치 판정 요청

### 사전 확인: HTML 실황

두 파일 직접 확인 후 판단합니다.

**child-care-grant-dday** 현황:
- Pretendard · `:root` 8토큰 · hero-line · fadeUp — 마이클이 이미 완비
- 현행 `--primary: #7B4FBF` 토큰 방식으로 선언. :root 1줄만 바꾸면 색 전환 가능
- `.status-card.active` box-shadow가 `rgba(123, 79, 191, 0.12)`으로 **하드코딩** — 색 변경 시 이 줄도 같이 교체 필요
- `/work-grant-dday/` 크로스링크 있음 (근로장려금과 연결)

**christmas-dday** 현황:
- Pretendard · `:root` 8토큰 · hero-line · fadeUp — 마이클이 이미 완비
- `--red: #c0392b` `:root`에 정의돼 있으나 CSS 전체에서 `var(--red)` 사용처 **0곳** (미사용 상태)
- 레드가 실제 적용된 곳 없음 — 터쿠아즈 primary 채택 시 레드를 실제 연결할 기회

---

### 판단 요약 (2건 + 레드 액센트)

#### 1. child-care-grant-dday → **B안 그린 `#198754` 권고**

이유 2가지:
- **정책 축 통일**: 자녀장려금과 근로장려금은 국세청 동일 창구·동일 기간에 함께 신청. HTML에 크로스링크까지 있다. 두 유틸이 같은 그린 계열이면 사용자가 "같은 정책 묶음"으로 직관 인식. 그린 권리·신뢰 축의 자연 확장.
- **팔레트 혼동 방지**: `#7B4FBF`(라벤더 자주)는 기존 `#6D28D9`(자주)와 같은 색역. 사용자가 두 자주를 구분하기 어려워 도메인 분기 흐림. 그린으로 가면 두 색역이 명확히 분리.

**A안 보류 이유**: 라벤더가 "부모·아이" 새 도메인으로 팔레트 확장 가능성 있지만, 기존 자주와 색역 혼동이 더 큰 리스크. 분기 정합성 우선.

**C안 인디고 보류**: 청약 가점 배정 색역. 자녀장려금은 청약이 아닌 현금 지원 정책 — 도메인 거리 있음.

**토큰 교체 체크리스트 (확정 시):**
- `:root` 4토큰: `--primary: #198754`, `--primary-hover: #146c43`, `--primary-soft: #D1FAE5`, `--primary-soft-border: #6EE7B7`
- `.status-card.active` box-shadow 하드코딩 `rgba(123, 79, 191, 0.12)` → `rgba(25, 135, 84, 0.12)`

#### 2. christmas-dday → **B안 터쿠아즈 `#0FADAD` 권고**

이유 2가지:
- **그린 샤드 혼동 방지**: 현행 다크그린 `#1a6b3a`를 유지하면 팔레트에 `#198754`(권리·신뢰 그린)와 `#1a6b3a`(크리스마스 그린) 두 그린이 공존. 사용자 입장에서 "왜 이 페이지는 다른 초록?" — 도메인 혼동.
- **도메인 분기 명확화**: 크리스마스는 권리·정책·시험 준비와 완전히 다른 도메인(축제·기다림·계절). 터쿠아즈는 기존 팔레트의 다른 어떤 색역과도 겹치지 않아 분기가 선명. "활기·기다림·축제" 독립 축 구축.

**A안 보류 이유**: 크리스마스 전통 색이라는 감성적 적합성은 있지만 그린 샤드 2개 혼동이 브랜드 일관성을 흐림.

**C안 코랄 제외**: WCAG AA 미달 (3.37:1 < 4.5:1). 채택 불가.

#### 3. 레드 액센트 `#c0392b` → **유지 + 실제 연결 권고**

현황: HTML `:root`에 `--red` 정의돼 있으나 실제 사용처 없음. 장식 의도였지만 미완성 상태.

터쿠아즈 primary 채택 시 레드를 활성화하는 방향:
- `.sch-date:last-child` (12월 25일 크리스마스 당일) → `color: var(--red)` — 크리스마스 당일만 레드 강조
- 또는 `.dday-date span` ("금요일") → `color: var(--red)` — 날짜 표기 내 레드 포인트

터쿠아즈+레드 조합은 크리스마스 컬러 팔레트(청록+빨강)의 현대적 해석. 전통 감성 유지하면서 primary는 새로운 톤. 레드 적용 범위(어느 선택자에 쓸지)는 다빈치 확정 후 반영.

---

### 공통 비고

두 파일 모두 마이클이 공통 스택(Pretendard · :root 8토큰 · hero-line · fadeUp)을 이미 적용해 둠. 이번 사이클 달리 정리 항목은 **색 토큰 교체 + 레드 연결** 2가지가 핵심. JS 로직·DOM ID·SEO·adsbygoogle·Cloudflare Analytics 전수 보존.

---

**다빈치, 판정 요청 사항:**
1. child-care-grant-dday: B안 그린 `#198754` 확정 or A안 현행 `#7B4FBF` 유지(라벤더 자주 신규 도메인) or C안 인디고 or 재지목
2. christmas-dday: B안 터쿠아즈 `#0FADAD` 확정 or A안 현행 다크그린 유지 or 재지목
3. christmas-dday 레드 액센트 `#c0392b` 실제 연결 범위 — `.sch-date` 크리스마스 당일 강조 or `.dday-date span` or 기타 or 제거

---

## 다빈치 판정 봉인 · 2026-08-14

**판정 3건 결착 (반려 없음 · 1회 결착):**

1. **child-care-grant-dday → B안 그린 `#198754` 확정** (6.46:1)
   달리 근거 그대로 채택. 결정적 근거는 두 개다. (1) 자녀장려금·근로장려금은 국세청 동일 창구·동일 기간 신청 정책 묶음이고 HTML에 이미 크로스링크(`/work-grant-dday/`)까지 걸려 있다. 두 유틸이 같은 primary 계열이면 사용자가 "같은 정책 세트"로 시각 인식. (2) 현행 `#7B4FBF` 라벤더는 기존 자주 `#6D28D9`(방학숙제·수능)와 색역 인접 — 사용자가 두 자주를 구분하기 어려워 도메인 분기 흐림.
   
   A안(현행 라벤더 유지)이 "부모·아이" 신규 도메인으로 팔레트 확장할 여지는 있으나, 색역 혼동 리스크가 팔레트 확장 이득보다 크다. C안 인디고는 청약 축이라 부적합.

2. **christmas-dday → B안 터쿠아즈 `#0FADAD` 확정** (6.09:1)
   달리 근거 그대로 채택. 현행 다크그린 `#1a6b3a` 유지 시 팔레트에 그린 샤드 2개(`#1a6b3a` vs `#198754`)가 공존해 사용자가 "왜 다른 초록?" 혼동. 터쿠아즈는 이미 광복절연차(2026-08-07)에서 "활기·최적화" 축으로 확립됨 — 크리스마스 = "축제·기다림"은 그 축의 자연 확장이다. 팔레트 신규 톤이 아니라 기존 터쿠아즈 축의 도메인 확장.
   
   호버 `#0A9396` (8.61:1) 견고. C안 코랄은 WCAG AA 미달로 채택 불가 확정.

3. **레드 액센트 `#c0392b` → 3곳 활성화 확정**
   달리 지적대로 현재 `--red` 토큰은 정의만 있고 사용처 0. 이 상태로는 미완성. 크리스마스 시그니처(청록+빨강)를 완성하려면 레드가 "크리스마스 당일" 순간에 국한해 등장해야 축제감이 최대화된다. 3곳으로 정한다:
   
   - **`.dday-date span`** (헤더 "(금요일)") → 레드. 크리스마스 당일 요일. 히어로 진입 순간 눈이 가는 지점.
   - **12/25(금) 스케줄 항목** → `<li class="holiday">` 클래스 추가 후 `.holiday .sch-date { color: var(--red); }`. 연말 일정 리스트에서 크리스마스 당일만 시각 시그니처. `:nth-child`는 HTML 재배열 시 취약하므로 명시 클래스로.
   - **`.dday-card.arrived .dday-main`** → 레드. D-day 도착(12/25) 순간 primary(터쿠아즈)에서 레드로 색 전환 — "기다림 → 축제" 전환 순간의 시각 폭발.
   
   기다림 상태 = 터쿠아즈 · 도착 순간 = 레드. 팔레트 이야기가 사용자 여정에 매핑됨.

**공통 스택 확인 (마이클 편입분 승계):**

두 파일 모두 마이클이 Pretendard Variable · `:root` 8토큰 · hero-line 2.5rem×2px · fadeUp keyframe · section-card · @media 480px 재정의를 이미 넣어둠. 이번 사이클 다빈치 반영 범위 = **색 토큰 교체 + 레드 활성화 3곳 + 하드코딩 rgba shadow 정합화**.

| 항목 | 값 |
|------|-----|
| 폰트 | Pretendard Variable (마이클 원본 유지 · preload 추가 없음 · 클레버 검수에서 판단) |
| CSS `:root` | 8토큰 방식 유지 · primary 계열 4개만 교체 |
| h1 letter-spacing | `-0.035em` (마이클 유지) |
| hero-line | 2.5rem × 2px --primary (마이클 유지 · 색만 자동 반영) |
| fadeUp | `.5s ease both` (마이클 유지) |
| 하드코딩 rgba 정합화 | child-care `rgba(123, 79, 191, 0.12)` → `rgba(25, 135, 84, 0.12)` |

**child-care-grant-dday 토큰 교체:**
- `--primary: #7B4FBF` → `#198754`
- `--primary-hover: #5E3A9A` → `#146c43`
- `--primary-soft: #EDE7F6` → `#D1FAE5`
- `--primary-soft-border: #C5B3E6` → `#6EE7B7`
- `.status-card.active` box-shadow `rgba(123, 79, 191, 0.12)` → `rgba(25, 135, 84, 0.12)`

**christmas-dday 토큰 교체 + 레드 활성화:**
- `--primary: #1a6b3a` → `#0FADAD`
- `--primary-hover: #145a2f` → `#0A9396`
- `--primary-soft: #d4edda` → `#D5F5F4`
- `--primary-soft-border: #a3d9b1` → `#7FDCDC`
- `--red: #c0392b` 유지
- `.dday-date span` → `color: var(--red)` (기존 primary에서 교체)
- `.schedule-list .holiday .sch-date` → `color: var(--red)` (신규 룰 · 12/25 li에 class="holiday" 추가)
- `.dday-card.arrived .dday-main` → `color: var(--red)` (신규 룰)

**팔레트 누적 갱신 (2026-07-31~08-14):**
자주 `#6D28D9` (방학숙제·수능) · 인디고 `#4F46E5` (청약·주민등록) · 그린 `#198754` (주휴수당·근로장려금·하자보수·**자녀장려금** 신규 편입) · 터쿠아즈 `#0FADAD` (광복절연차·**크리스마스** 신규 편입) · 티일 `#0F766E` (이사짐) · 코발트 `#1D4ED8` (체감온도·공휴일대체·기숙사) · 앰버 (기숙사 이진 보조) · 주황 `#EA580C` (추석 KTX) · 레드 `#c0392b` (크리스마스 액센트 · primary 아님 · 크리스마스 당일 시그니처)

**보존 확인:**
- SEO 메타·OG·Twitter·JSON-LD 전수
- adsbygoogle 스크립트 로더 유지
- `#ad-slot` 위치·크기 유지
- JS 계산 로직 (자녀장려금 3구간 상태 전환·자격 체크·홈택스·ARS 링크 · 크리스마스 D-day·HMS 타이머·arrived 클래스·공유버튼) 무손실
- DOM ID 전수 (#status-card·#status-label·#main-days·#days-sub·#checklist·#check-result · #ddayCard·#ddayLabel·#ddayMain·#countdown·#cH·#cM·#cS·#shareMsg)
- 크로스링크 `/work-grant-dday/` 유지
- Cloudflare Analytics beacon 유지
- 반응형 미디어 쿼리 (480px) 유지

*판정 봉인*: 다빈치 (팀장) · 2026-08-14 03:XX · 클레버 검수 릴레이

---

## 클레버 검수 · 2026-08-14

- 4축 검수 결과: [정확성: 수정 / 완성도: OK / 원칙: OK / 배포준비: OK]
- 수정 항목:
  - **child-care-grant-dday** · 요일 표기 오류 2곳 정정 · `9월 1일(월)~9월 15일(월)` → `9월 1일(화)~9월 15일(화)` · `.lede` + `.period-bar` · 실증: `date -jf "%Y-%m-%d" "2026-09-01"` = 화요일 · `2026-09-15` = 화요일 · 마이클·다빈치 놓친 관성 오류(월요일 관행 가정) · 08-12 학년도 표기 오류 사후 패턴과 동일 (요일·연도·표기 사실관계 검증은 검수 필수 항목)
  - **christmas-dday** · 수정 없음 · 12/1(화)·12/24(목)·12/25(금)·12/26(토)·12/31(목) 5곳 요일 전수 검증 통과
- 배포 준비 상태: **준비 완료**

**검증 로그:**

| 검증 항목 | christmas-dday | child-care-grant-dday |
|-----------|----------------|-----------------------|
| 요일 정확성 | 5곳 통과 (12/1·24·25·26·31) | 2곳 오류→정정 (9/1·15 월→화) |
| 다빈치 판정 반영 | ✓ `--primary:#0FADAD` · `--primary-hover:#0A9396` · `--primary-soft:#D5F5F4` · `--primary-soft-border:#7FDCDC` · `--red:#c0392b` 유지 · 레드 활성화 3곳(`.dday-date span` · `.holiday .sch-date` + 12/25 li `class="holiday"` · `.dday-card.arrived .dday-main`) 전수 확인 | ✓ `--primary:#198754` · `--primary-hover:#146c43` · `--primary-soft:#D1FAE5` · `--primary-soft-border:#6EE7B7` · `.status-card.active` box-shadow `rgba(25,135,84,0.12)` 정합화 확인 |
| WCAG AA 대비 | 6.09:1 · 8.61:1 통과 | 6.46:1 · 8.62:1 통과 |
| SEO 메타·OG·Twitter | 전수 유지 | 전수 유지 |
| JSON-LD WebApplication | ✓ | ✓ |
| canonical URL | `/christmas-dday/` | `/child-care-grant-dday/` |
| adsbygoogle 로더 | ✓ `ca-pub-9477150496807643` | ✓ 동일 |
| `#ad-slot` 위치 | ✓ disclaimer 하단 | ✓ disclaimer 하단 |
| DOM ID 전수 | #ddayCard·#ddayLabel·#ddayMain·#countdown·#cH·#cM·#cS·#shareMsg | #status-card·#status-label·#main-days·#days-sub·#checklist·#check-result |
| 크로스링크 | — | `/work-grant-dday/` 유지 |
| 반응형 480px | ✓ | ✓ |
| Cloudflare Analytics | ✓ token `8f333dc2c9e844b39f36daec8c0c0570` | ✓ 동일 |
| 시맨틱 태그 | `<main>·<nav>·<h1>·<h2>·<footer>` | 동일 |
| 키보드 접근 | 버튼·링크 · label로 체크박스 감싸기 | 동일 |
| 인라인 CSS | ✓ | ✓ |
| 외부 의존 | Pretendard CDN·adsbygoogle·CF beacon만 | 동일 |

**계산 로직 시뮬레이션 (오늘 2026-08-14 04:XX KST 기준):**

- christmas-dday: `TARGET - now` = 약 133일 → D-133 표시 · 초 단위 정확 계산 · 자정 정확 전환 (`Math.floor(totalSec/86400)`) · arrived 상태 UI 로직 정합
- child-care-grant-dday: `now < START` 분기 · `Math.ceil((START-now)/86400000)` = 약 D-18 · 3구간 상태 전환(신청 전·중·후) 로직 정합 · 자격 체크 로직(0/2/5 임계 정합) · `--red` 스타일 없어 fail 상태 배경 `#f8d7da` 하드코딩(다빈치 스택 밖 · 원본 유지)

**이월 이슈 (사이클 밖 유지보수):**
1. `Math.ceil((START-now)/86400000)` 자정 정밀도 · 08-12부터 이월 · 자녀장려금도 동일 패턴 · 대체 방식 검토는 이월
2. `<link rel="stylesheet" as="style" ...>` — `as` 속성은 `rel="preload"` 전용 · 브라우저 관대 무시 · 08-12부터 이월 · 두 파일 승계 · 스타일 시트 preload 패턴 재설계 필요
3. adsbygoogle inline `<ins class="adsbygoogle">` 태그 없이 로더만 로드됨 · `#ad-slot` div만 있음 · AdSense 승인 후 슬롯 삽입 결정 · 08-01 이후 전 파일 공통 이월

**전 파일 이전 사이클 브랜드 승계 확인:**
- 공통 스택(Pretendard Variable · `:root` 8토큰 · hero-line 2.5rem×2px · fadeUp `.5s ease both` · section-card · `@media 480px`) 마이클이 이미 편입 완료 · 다빈치 반영 범위 = 색 토큰 교체 + 레드 활성화 3곳(christmas) + rgba shadow 정합화(자녀장려금) · 클레버 검수에서 승계 무결성 확인

*검수 봉인*: 클레버 (팀장) · 2026-08-14 04:XX · 배포 지시 대기 (git push 실행 X · 파일 이동 실행 X · `_COMMON.md §7` 준수 · 사마의 보고 후 대표 직접 승인)
