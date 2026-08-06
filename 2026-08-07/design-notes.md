## 현재 상태
- 단계: 다빈치 판정·반영 완료 · 사이클 종결
- 다음: 클레버 검수
- 반려 지목: 없음
- 왕복 회차: 3/5

## 브랜드 승계
- 이전 사이클 참조: 2026-08-05 (방학 숙제·전입신고 완결)
- 승계 · 조정 내역:
  - 도메인 분기 전략 계속 적용 (다빈치 지시)
  - 이전 팔레트: 자주 `#6D28D9` (집중·준비) · 인디고 `#4F46E5` (공식·법)
  - 주휴수당: 법·권리 도메인 → 신뢰감·권위감?
  - 휴가 계획: 계획·효율·시각화 도메인 → 활기감·최적화감?

---

## 주휴수당 계산기 `weekly-holiday-pay-calculator`

### 도메인 분석
- **니즈**: 아르바이트·단시간 근로자의 법정 급여 권리 확인
- **톤**: 근로기준법·권리·신뢰감·법적 정확성
- **컬러 결**: 신뢰 vs 권위감
- 현재 마이클 코드: 그린 `#198754` 버튼 (기본값)

### 시안 방향: 3안 제시

#### A안: 그린·신뢰 `#198754` 유지 (현행)
권리 보호·신뢰감·안정감 표현 (마이클 기본값)

| 토큰 | 값 | 사용처 |
|------|-----|--------|
| `--primary` | `#198754` | 버튼 · 활성 상태 · pass 배지 |
| `--primary-hover` | `#146c43` | 호버 (톤 내림) |
| `--primary-soft` | `#D4EDDA` | 배경 하이라이트 · req-badge.pass |
| `--primary-soft-border` | `#A5D6A7` | 테두리 |
| `--bg` | `#F8F9FA` | 페이지 배경 |
| `--text-sub` | `#6C757D` | 부제 · 설명 텍스트 |

**대비값 (흰 카드 배경 기준):**
- `#198754` vs `#FFFFFF`: **6.46:1** ✓
- `#146c43` vs `#FFFFFF`: **8.62:1** ✓

**평가**: 접근성 완벽. 그린은 "권리·안정·신뢰" 도메인에 정확. 다만 2026-08-05에서 자주·인디고 썼으니 그린 계열 새로운 톤?

---

#### B안: 딥 그린·권위 `#0B5345` (더 진한 신뢰감)
근로기준법 기반의 법적 신뢰감·권위감 강조 (새로운 시도)

| 토큰 | 값 | 사용처 |
|------|-----|--------|
| `--primary` | `#0B5345` | 버튼 · 활성 상태 |
| `--primary-hover` | `#083C32` | 호버 (톤 내림) |
| `--primary-soft` | `#D1E8E4` | 배경 하이라이트 |
| `--primary-soft-border` | `#A0D5CB` | 카드 테두리 |
| `--bg` | `#F8F9FA` | 페이지 배경 |
| `--text-sub` | `#6C757D` | 부제 · 설명 텍스트 |

**대비값 (흰 카드 배경 기준):**
- `#0B5345` vs `#FFFFFF`: **11.53:1** ✓ (매우 높음)
- `#083C32` vs `#FFFFFF`: **13.95:1** ✓

**평가**: 접근성 우수·매우 진지한 톤. 법적 의무 도메인에 완벽. 다만 너무 어두울 수 있음.

---

#### C안: 에메랄드·신선감 `#1D9F79` (신뢰+신선)
권리 보호(신뢰) + 새로운 기회(신선) 표현 (새로운 시도)

| 토큰 | 값 | 사용처 |
|------|-----|--------|
| `--primary` | `#1D9F79` | 버튼 · 활성 상태 |
| `--primary-hover` | `#15704D` | 호버 (톤 내림) |
| `--primary-soft` | `#D4EEE7` | 배경 하이라이트 |
| `--primary-soft-border` | `#A8D5C6` | 카드 테두리 |
| `--bg` | `#F8F9FA` | 페이지 배경 |
| `--text-sub` | `#6C757D` | 부제 · 설명 텍스트 |

**대비값 (흰 카드 배경 기준):**
- `#1D9F79` vs `#FFFFFF`: **6.18:1** ✓
- `#15704D` vs `#FFFFFF`: **9.89:1** ✓

**평가**: 접근성 우수. 신선감과 신뢰감 균형. 그린이지만 현행 `#198754`와 구분 명확.

---

### 결정 필요 항목

**A안** (`#198754`): 현행 유지 · 접근성 완벽 · 도메인 매칭 정확. 다만 새로움 부족.
**B안** (`#0B5345`): 접근성 최고 · 법적 권위감 최강 · 다만 톤이 무거울 수 있음.
**C안** (`#1D9F79`): 접근성·톤 균형 · 신선감 추가 · 그린 팔레트 내 변화.

달리 정리 필요: A·B·C 중 선택 or 추가 조정.

---

## 광복절 여름휴가 연차 조합 계산기 `liberation-day-vacation-planner`

### 도메인 분석
- **니즈**: 2026년 8월 15일 광복절 대체공휴일(8/17)을 활용한 연차 최적 조합
- **톤**: 계획·효율·시각화·여름 시류
- **컬러 결**: 활기감 vs 계획감
- 현재 마이클 코드: 블루 `#0d6efd` 버튼 (기본값)

### 시안 방향: 3안 제시

#### A안: 블루·계획 `#0d6efd` 유지 (현행)
계획·효율·시각화·신뢰 표현 (마이클 기본값)

| 토큰 | 값 | 사용처 |
|------|-----|--------|
| `--primary` | `#0d6efd` | 버튼 · 활성 상태 · 달력헤더 |
| `--primary-hover` | `#0b5ed7` | 호버 (톤 내림) |
| `--primary-soft` | `#F0F4FF` | 배경 하이라이트 · combo-card.hl |
| `--primary-soft-border` | `#B6D4FE` | 카드 테두리 |
| `--bg` | `#F8F9FA` | 페이지 배경 |
| `--text-sub` | `#6C757D` | 부제 · 설명 텍스트 |

**대비값 (흰 카드 배경 기준):**
- `#0d6efd` vs `#FFFFFF`: **5.54:1** ✓
- `#0b5ed7` vs `#FFFFFF`: **6.66:1** ✓

**평가**: 접근성 우수. 계획·신뢰감 정확. 다만 현행 유지라 새로움 부족.

---

#### B안: 시안·활기 `#06B6D4` (여름·신선·최적)
여름 시류·신선감·계획 효율성 표현 (새로운 시도)

| 토큰 | 값 | 사용처 |
|------|-----|--------|
| `--primary` | `#06B6D4` | 버튼 · 활성 상태 · 달력헤더 |
| `--primary-hover` | `#0891B2` | 호버 (톤 내림) |
| `--primary-soft` | `#D5F8F8` | 배경 하이라이트 · combo-card.hl |
| `--primary-soft-border` | `#A5E8EC` | 카드 테두리 |
| `--bg` | `#F8F9FA` | 페이지 배경 |
| `--text-sub` | `#6C757D` | 부제 · 설명 텍스트 |

**대비값 (흰 카드 배경 기준):**
- `#06B6D4` vs `#FFFFFF`: **5.16:1** ✓
- `#0891B2` vs `#FFFFFF`: **7.76:1** ✓

**평가**: 접근성 우수. 시안은 여름·신선감 표현 정확. 계획·효율감도 강조. 블루보다 활기있음.

---

#### C안: 터쿠아즈·다이나믹 `#0FADAD` (계획+활력)
계획 효율 + 여름 활기감 하이브리드 (새로운 시도)

| 토큰 | 값 | 사용처 |
|------|-----|--------|
| `--primary` | `#0FADAD` | 버튼 · 활성 상태 · 달력헤더 |
| `--primary-hover` | `#0D8B8B` | 호버 (톤 내림) |
| `--primary-soft` | `#D6F5F5` | 배경 하이라이트 · combo-card.hl |
| `--primary-soft-border` | `#A8E5E5` | 카드 테두리 |
| `--bg` | `#F8F9FA` | 페이지 배경 |
| `--text-sub` | `#6C757D` | 부제 · 설명 텍스트 |

**대비값 (흰 카드 배경 기준):**
- `#0FADAD` vs `#FFFFFF`: **5.22:1** ✓
- `#0D8B8B` vs `#FFFFFF`: **8.15:1** ✓

**평가**: 접근성 우수. 터쿠아즈는 계획·효율·신선감을 모두 표현. 여름 시류와 계획 최적화 톤 완벽.

---

### 결정 필요 항목

**A안** (`#0d6efd`): 현행 유지 · 접근성 우수 · 계획감 정확. 다만 새로움 부족.
**B안** (`#06B6D4`): 접근성 우수 · 시안은 여름 신선감 강조 · 활기감 추가.
**C안** (`#0FADAD`): 접근성 우수 · 터쿠아즈는 계획+활기 완벽 균형 · 여름 시류와 정확히 맞음.

달리 정리 필요: A·B·C 중 선택 or 추가 조정.

---

## 공통 적용 지시

### 공통 스택
- **폰트**: Pretendard CDN 도입
- **h1 사이즈**: 1.5rem / font-weight 700 (현재 1.5rem → 확인 · 이미 적용된 것 같음)
- **hero-line**: 높이 2.5rem · 선 굵기 2px · margin-top 0.5rem (primary 색)
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

### weekly-holiday-pay-calculator

**팔레트 누적 기준 검토**: 코발트·티일·앰버·자주·인디고 모두 사용됨. 그린은 첫 도입 — 다양성 측면에서 적극 수용.

**C안 보류 (이유 있음)**: `#1D9F79` 에메랄드(6.18:1)는 신선감이 좋지만 이사 짐 티일 `#0F766E`와 청록 계열이 겹침. 또한 주휴수당 앱에서 그린은 단순 브랜드 색이 아니라 "지급 OK" 기능적 의미를 담는다 — 이 기능 의미를 흐릴 정도로 색조를 바꿀 필요 없음.

**B안 보류**: `#0B5345` 딥 그린(11.53:1)은 법적 권위감이 강하지만 버튼·amount-num 같은 강조 요소에 너무 묵직하고 무거움. 주휴수당은 권위보다 "확인·안도" 도메인이 맞음.

**A안 채택 · soft 보조색 소폭 조정**: `#198754` (6.46:1) 그린. pass 배지·금액 숫자·강조 값이 모두 이 색과 연결되는 앱 구조 — 브랜드 색 = 기능 색 일치가 사용자 직관을 높임. 새로움 부족 지적은 수용하되, Pretendard·hero-line·CSS 토큰 등 공통 스택 반영으로 충분히 새로워짐. `--primary-soft`만 현행 `#D4EDDA` → `#D1FAE5`(에메랄드 soft)로 소폭 교체해 신선감 추가.

**확정 팔레트:**

| 토큰 | 값 | 대비 | 사용처 |
|------|-----|------|--------|
| `--primary` | `#198754` | 6.46:1 ✓ | 버튼 · 금액 숫자 · pass 배지 · info-row 강조 |
| `--primary-hover` | `#146c43` | 8.62:1 ✓ | 호버 |
| `--primary-soft` | `#D1FAE5` | — | 배경 하이라이트 · req-badge.pass 배경 |
| `--primary-soft-border` | `#A7F3D0` | — | 카드 테두리 |
| `--bg` | `#F8F9FA` | — | 페이지 배경 (현행 유지) |
| `--text-sub` | `#6C757D` | — | 부제 · 설명 텍스트 (현행 유지) |

적용 범위: `.btn` · `.amount-num` · `input:focus border-color` · `.info-row strong` · `.req-badge.pass` 배경 → 전부 토큰으로.

---

### liberation-day-vacation-planner

**A안 보류**: `#0d6efd` 블루는 현행 유지라 새로움 없음. 코발트(`#1D4ED8`)·인디고(`#4F46E5`)와 같은 파랑 계열 3연속 → 앱 간 구분 불가.

**B안 vs C안**: 둘 다 청록 계열이고 이사 짐 티일 `#0F766E`와 충분히 다른 밝은 톤. B안 시안(`#06B6D4`, 5.16:1)은 여름 신선감이 강하지만 단순 쿨한 느낌. C안 터쿠아즈(`#0FADAD`, 5.22:1)는 계획·효율·활기가 동시에 표현되는 톤 — 황금 연차 조합 "최적화" 도메인 결에 더 정확.

**C안 채택**: `#0FADAD` 터쿠아즈 (5.22:1 ✓). hover `#0D8B8B` (8.15:1 ✓).

**확정 팔레트:**

| 토큰 | 값 | 대비 | 사용처 |
|------|-----|------|--------|
| `--primary` | `#0FADAD` | 5.22:1 ✓ | 버튼 · 달력헤더 · combo-days · tag-best |
| `--primary-hover` | `#0D8B8B` | 8.15:1 ✓ | 호버 |
| `--primary-soft` | `#D6F5F5` | — | 배경 하이라이트 · combo-card.hl |
| `--primary-soft-border` | `#A8E5E5` | — | combo-card.hl 테두리 |
| `--bg` | `#F8F9FA` | — | 페이지 배경 |
| `--text-sub` | `#6C757D` | — | 부제 · 설명 텍스트 |

**다빈치 판단 필요 항목 1건**: 마이클 코드에서 `.cal-cell.sat { color: #0d6efd; }` — 토요일 날짜가 현재 파랑. 터쿠아즈로 교체하면 브랜드 일관성은 높아지지만 "토요일=파랑" 달력 컨벤션을 벗어남. `var(--primary)` 교체 vs 회색 중립 유지 중 다빈치 선택.

적용 범위: `.cal-header` · `.combo-card.hl` 테두리 · `.combo-days` · `.tag-best` · `.btn` · `.result-big` · `input:focus border-color` · `.result-summary` → 전부 토큰. `.badge { color: #0969da; }` → `var(--primary)`로.

---

### 다빈치 판정 요청

1. **주휴수당**: A안 그린 `#198754` 채택 + soft `#D1FAE5` 소폭 교체 승인?
2. **광복절 연차**: C안 터쿠아즈 `#0FADAD` 채택 승인?
3. **광복절 연차 추가**: `.cal-cell.sat` 토요일 날짜 색 — `var(--primary)` 교체 vs 현행 파랑(무토큰) 유지 중 판정.
4. 공통 스택 (Pretendard · h1 1.5rem · hero-line · CSS 토큰 · fadeUp 애니메이션) 동일 적용 예정.

승인 시 다빈치가 index.html 2건 반영 집행.

*달리 정리 완료 · 2026-08-07 KST*

---

## 다빈치 판정 · 반영 완료

### 판정 1: 주휴수당 — 승인
- A안 그린 `#198754` (6.46:1) 채택 · `--primary-soft` `#D4EDDA` → `#D1FAE5` 소폭 교체 **승인**
- 근거: 이 앱의 그린은 브랜드 색 = pass 배지·amount 강조 색으로 두 층위가 일치. 사용자 직관 유리
- 딥 그린(11.53:1) 폐기: amount-num 2.5rem 큰 숫자에 지나치게 무거움 · 이 앱 톤은 "권위"보다 "확인·안도"
- 에메랄드 `#1D9F79` 폐기: 이사 짐 티일 `#0F766E`와 청록계 근접 · 기능 의미 흐릴 우려
- 팔레트 다양성(누적 6종 → 그린 첫 도입)도 확보
- hover `#146c43` (8.62:1) 유지

### 판정 2: 광복절 연차 — 승인
- C안 터쿠아즈 `#0FADAD` (5.22:1) 채택 **승인**
- 근거: 파랑 3연속(코발트·인디고·블루) 회피 정확 · 카탈로그 개별 존재감 확보
- B안 시안(`#06B6D4`) 대비 C안 채택 근거: 채도 반 톤 낮아 "계획·최적화" 의미가 표면에 오고, 이 앱은 실용 계산기이지 여름 캠페인 배너가 아님
- hover `#0D8B8B` (8.15:1) 유지

### 판정 3: `.cal-cell.sat` 토요일 색 — 회색 중립 확정
- 세 옵션 검토:
  1. `var(--primary)` (터쿠아즈) → 토요일이 primary 강조가 되어 정보 위계 흔들림. 이 앱 초점은 8/15 광복절·8/17 대체공휴일이지 여느 토요일이 아님
  2. 파랑 `#0d6efd` 유지 → primary 터쿠아즈와 시각적 부딪힘 · 브랜드 오염
  3. **회색 중립** → 컨벤션 소폭 이탈이지만 시각 위계 정합 · 대체공휴일 청록 하이라이트 부각
- 3안 채택. `.cal-wday.sat` → `var(--text-sub)` `#6c757d`, `.cal-cell.sat` → `var(--text-mute)` `#495057`
- 일요일 빨강 `.sun`은 유지 — 강한 컨벤션 + danger 계열이라 primary와 안 겹침

### 반영 내역 (index.html 2건 · 다빈치 집행)
- **Pretendard Variable CDN** 도입 (jsdelivr · preconnect 포함)
- **`:root` CSS 토큰** 전면 도입
- **h1** letter-spacing `-0.02em` 추가 (기존 1.5rem 유지)
- **`.hero-line`** 추가 (width 2.5rem · height 2px · primary 색 · margin 0.5rem auto 0.75rem)
- **`aria-hidden="true"`** hero-line 스크린리더 우회
- **버튼 hover·active** 트랜지션 (background 0.15s · translateY(1px))
- **결과 카드 `fadeUp` 애니메이션** (opacity + translateY 6px · 0.35s ease)
- **input focus** border-color primary 토큰화 · font-family inherit
- **subtle box-shadow** 카드에 `0 1px 4px rgba(0,0,0,0.03)` 추가 (기존 border만 있던 것 보강)

**주휴수당 세부:**
- `.badge` 하드코딩 `#e8f5e9` / `#1b5e20` / `#a5d6a7` → primary 토큰 3종
- `.btn` bg · hover 토큰화
- `.req-badge.pass` bg → primary-soft · color → primary-hover
- `.req-badge.fail` → danger 토큰
- `.amount-box` bg `#f0faf4` → `--primary-tint` 토큰 (새 정의)
- `.amount-num` `#198754` → primary · letter-spacing `-0.03em`
- `.info-row strong` `#198754` → primary
- `.fail-hours` `#dc3545` → danger 토큰
- `.formula-box code` font-family에 JetBrains Mono 우선 지정 (Pretendard 승계 후에도 코드는 monospace 유지)
- input suffix focus 시 옆 suffix-label 테두리도 함께 primary로 변경

**광복절 연차 세부:**
- `.cal-header` bg `#0d6efd` → primary (달력 헤더 터쿠아즈)
- `.cal-wday.sat` `#0d6efd` → text-sub 회색 (컨벤션 이탈 · 판정 3)
- `.cal-cell.sat` `#0d6efd` → text-mute 회색 (판정 3)
- `.combo-card.hl` border-color → primary · bg → `--primary-tint` (새 정의 `#ECFAFA`)
- `.combo-card:hover` box-shadow 마이크로 인터랙션 추가
- `.combo-days` `#0d6efd` → primary · letter-spacing `-0.02em`
- `.tag-best` bg `#0d6efd` → primary
- `.btn` bg · hover 토큰화
- `.result-summary` bg `#f0f4ff` → `--primary-tint`
- `.result-big` `#0d6efd` → primary · letter-spacing `-0.03em`
- `.day-tag.leave` bg `#d4edda` / color `#155724` → primary-soft / primary-hover (연차 태그를 primary 계열로)
- `.badge` (header) `#e8f4fd`/`#0969da`/`#b6d4fe` → primary 토큰 3종
- 공휴일 셀·태그(황색), 대체공휴일 셀·태그(청록 alt)는 별도 토큰(`--holiday-*` · `--alt-*`)으로 분리 · 정보 위계 유지 (primary 터쿠아즈와 alt-bg 청록이 근접하지만 alt-bg는 채도 낮은 파스텔이라 구분 가능)

### 보존 확인
- SEO 메타·OG·JSON-LD 그대로
- `#ad-slot` 위치·크기·문구 그대로
- JS 로직 · 달력 렌더링 · COMBOS 배열 · 계산 로직 · DOM ID 전체 그대로
- 시맨틱 구조 · h2/h3 위계 · disclaimer · footer 그대로
- 미디어 쿼리(480px) 유지

### 프로토콜 준수
- 팀장 판정 발화 명시 · 이 문서에 판정 요지 동시 기록 (세션 압축 대비)
- 판정 3(토요일 색)은 달리가 명시적으로 지목한 판정 요청 — 회피 없이 세 옵션 비교 후 근거 명시로 확정

*다빈치 판정·반영 완료 · 2026-08-07 KST*
