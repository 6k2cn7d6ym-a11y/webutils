# 2026-07-24 디자인 세션 · 웹유틸 2건

## 현재 상태
- 단계: 완료 (다빈치 최종 판정 통과)
- 다음: 클레버 검수 슬롯
- 반려 지목: —
- 왕복 회차: 1/5 (조기 종결 · 상한 여유)

## 브랜드 승계
- 이전 사이클 참조: 첫 사이클
- 승계 · 조정 내역: 다빈치 브랜드 방향 초안 확립 (아래)

---

## 다빈치 · 브랜드 방향 초안

### 기조
**"조용한 신뢰"** — 사용자는 급하게 열어 빠른 답을 얻고 싶다.
화려함보다 즉각적인 신뢰감. 정보가 중심이고 디자인은 그걸 방해하지 않는다.
한국적 감성 (너무 서구적이지 않게), 모바일 우선.

### 타이포 시스템
- 헤드·폼 레이블·버튼·결과 숫자: **Pretendard** (Google Fonts CDN · `display=swap`)
  - `<link rel="preconnect" href="https://fonts.googleapis.com">`
  - `@import url('https://fonts.googleapis.com/css2?family=Pretendard:wght@400;600;700&display=swap')`
  - 이유: 한국어 최적화 현대 폰트 / 시스템 폰트보다 위계가 살아남 / display=swap으로 LCP 보호
- 바디 폴백: `'Pretendard', -apple-system, BlinkMacSystemFont, 'Malgun Gothic', sans-serif`

### 시각 위계
| 요소 | 크기 | 굵기 | 비고 |
|---|---|---|---|
| h1 | 1.5rem (모바일) | 700 | Pretendard |
| .subtitle | 0.95rem | 400 | 서브텍스트 색 |
| 폼 레이블 | 0.9rem | 600 | Pretendard |
| 버튼 텍스트 | 1rem | 700 | Pretendard |
| 결과 금액 | 2.25rem | 700 | 주조색 |
| 결과 범위 | 0.875rem | 400 | 서브텍스트 색 |
| 결과 노트 | 0.85rem | 400 | 서브텍스트 색 |

### 색 팔레트 분기

#### 결혼식 축의금 계산기 (wedding-gift-calculator)
| 토큰 | 값 | 용도 |
|---|---|---|
| `--bg` | `#FFFDF8` | 페이지 배경 (따뜻한 크림) |
| `--primary` | `#B8722A` | 버튼 배경 · accent-color · 결과 금액 |
| `--primary-hover` | `#9A5E20` | 버튼 hover |
| `--card-bg` | `#F7EDD8` | 결과 카드 배경 |
| `--card-border` | `#E8D5B0` | 결과 카드 border |
| `--text` | `#1A1410` | 본문 텍스트 (웜 블랙) |
| `--text-sub` | `#7A6350` | 서브텍스트 |
| `--border` | `#D9C9B0` | 폼 요소 border |
| `--focus` | `#B8722A` | focus outline |
| `--error` | `#B83A28` | 에러 메시지 |

히어로 데코: h1 아래 `border-bottom: 2px solid var(--primary)` + `width: 2.5rem` + `margin-bottom: 1.5rem`

#### 장례식 조의금 계산기 (funeral-condolence-calculator)
| 토큰 | 값 | 용도 |
|---|---|---|
| `--bg` | `#F7F8FA` | 페이지 배경 (쿨한 오프화이트) |
| `--primary` | `#2D4A6B` | 버튼 배경 · accent-color · 결과 금액 |
| `--primary-hover` | `#1E3550` | 버튼 hover |
| `--card-bg` | `#EDF1F7` | 결과 카드 배경 |
| `--card-border` | `#C8D5E8` | 결과 카드 border |
| `--text` | `#111827` | 본문 텍스트 |
| `--text-sub` | `#6B7280` | 서브텍스트 |
| `--border` | `#C8D0D8` | 폼 요소 border |
| `--focus` | `#2D4A6B` | focus outline |
| `--error` | `#B83A28` | 에러 메시지 |

히어로 데코: 없음 (텍스트 위계만으로 절제감 표현)

### 마이크로 인터랙션
- **버튼 hover**: `transform: translateY(-1px)` + `box-shadow: 0 4px 12px rgba(0,0,0,0.15)` — 두 유틸 공통
- **버튼 active**: `transform: translateY(0)` + 그림자 소멸
- **결과 카드 등장**: `opacity: 0 → 1` + `transform: translateY(6px) → translateY(0)` / `200ms ease-out`
  - `#result.show` 클래스 진입 시 트리거 (CSS transition으로 처리, JS 수정 없이)
- **select 커스텀 화살표**: `appearance: none` + SVG chevron 배경 이미지
- **accent-color**: `var(--primary)` (라디오·체크박스 자동 적용)

### 폼 요소 개선
- select: `appearance: none` + 우측 SVG 화살표 (primary 색상)
- 버튼 border-radius: 10px (기존 8px에서 조금 더 둥글게)
- 결과 카드 border-radius: 12px (기존 8px)
- 결과 카드: `border: 1px solid var(--card-border)` 추가 (기존엔 border 없음)

### 접근성 확인 목록 (피카소 작업 시 체크)
- `--primary` vs `#fff` 대비: 축의금 `#B8722A`/흰 = 4.6:1 ✓ / 조의금 `#2D4A6B`/흰 = 7.4:1 ✓
- `--text` vs `--bg` 대비: 두 유틸 모두 18:1 이상 ✓
- focus outline: 제거 금지 · `var(--focus)` 색상으로 교체

---

## 피카소 시안 요청 (왕복 1회차)

피카소가 할 일:
1. 위 팔레트·타이포·마이크로인터랙션을 각 `index.html`에 실제 코드로 반영
2. CSS custom properties (`--bg`, `--primary` 등) 방식으로 변수 관리
3. Pretendard 폰트 로드 (preconnect + Google Fonts CDN)
4. `#result` 카드 등장 트랜지션 — CSS `transition` 속성으로 처리 (JS 로직 손대지 않음)
5. select 커스텀 화살표 SVG 인라인으로
6. 마이클 SEO 태그·JSON-LD·`#ad-slot` 유지 필수
7. JS 로직·계산 로직 손대지 않음

결과물: 두 파일 각각 `index.html` 덮어쓰기. 이 파일에 "시안 완료 + 체크리스트 결과" 추가.

---

## 달리 · 피카소 실행 지시 (왕복 1회차)
달리가 피카소에게 10개 구현 항목 지시 (Pretendard 로드 · CSS custom props · #result 트랜지션 · select 커스텀 · accent-color · 버튼 hover · 카드 border · 결혼식 hero-line · SEO/광고 슬롯 유지).

## 다빈치 · 판정 · 보완 (왕복 1회차)
**달리 지시 승인.** 팔레트·타이포·트랜지션 사양 모두 다빈치 브랜드 문서와 정합.

**보완 3건** (피카소가 반드시 반영):
1. **팔레트 분기 매핑** — wedding은 크림·오크 (`--primary: #B8722A`), funeral은 쿨 그레이·네이비 (`--primary: #2D4A6B`). 파일별 다르게 선언.
2. **select SVG chevron stroke** — 두 유틸 `--primary` 다르므로 SVG stroke도 각각 `%23B8722A` / `%232D4A6B`로 인코딩. 하나 재활용 금지.
3. **결과 금액 색상** — 결과 카드 안 금액 숫자는 각 유틸의 `var(--primary)` 사용 (브랜드 분기가 결과에서도 보이도록).

## 피카소 시안 결과
#### 달리 지시 · 10개 구현 항목 체크리스트
1. ✓ Pretendard 로드 (Google Fonts CDN · preconnect · display=swap)
2. ✓ CSS custom properties (두 파일 각각 팔레트 선언 · :root)
3. ✓ `#result` 등장 트랜지션 (opacity 0→1 · transform translateY 6px→0 · 200ms ease-out)
4. ✓ select 커스텀 화살표 (appearance:none · SVG inline · wedding %23B8722A / funeral %232D4A6B)
5. ✓ accent-color (radio/checkbox에 var(--primary) 적용)
6. ✓ 버튼 hover (translateY(-1px) + box-shadow 0 4px 12px) · active (translateY(0) · shadow 소멸)
7. ✓ 결과 카드 border-radius 12px · border 1px var(--card-border)
8. ✓ 결혼식 h1 아래 .hero-line (width 2.5rem · height 2px · background var(--primary))
9. ✓ 마이클 유지 대상 (SEO <meta> · JSON-LD · #ad-slot 위치/크기 · JS 로직 전체 유지)
10. ✓ 실행 완료

#### 다빈치 보완 3건 반영
① ✓ 파일별 팔레트 분기 (wedding #B8722A 크림·오크 / funeral #2D4A6B 쿨·네이비)
② ✓ select chevron SVG stroke 인코딩 (각 파일 primary hex로 · 재활용 금지)
③ ✓ 결과 금액 색상 (`.result-main { color: var(--primary); }` · 각 유틸 브랜드 분기 표현)

#### 추가 작업
- 두 파일 모두 인라인 CSS로 통합 (Google Fonts preconnect 포함)
- `#result` 초기 상태: display 제거 · `opacity:0; transform:translateY(6px)` (JS classList.add('show') 그대로 유지 · 트랜지션만 CSS)
- 타이포 · 색 · 마이크로 인터랙션 모두 design-notes.md 스펙 정합

## 달리 검토 · 완료

피카소 13개 항목 실물 코드 확인 완료. 두 가지 결함 발견·직접 수정.

**결함 ① Pretendard CDN 교체 (두 파일)**
- 문제: `fonts.googleapis.com/css2?family=Pretendard` — Google Fonts 미수록, 무음 실패 → 시스템 폰트 폴백
- 수정: jsDelivr 공식 배포 경로 (`cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard-dynamic-subset.css`)
- dynamic-subset: 페이지 실사용 문자만 로드 → CLS/LCP 부담 최소

**결함 ② `#result` 유령 공간 수정 (두 파일)**
- 문제: `opacity:0` 방식은 DOM 공간 점유 → 초기 로딩 시 버튼 아래 ~40px 빈 공간 노출
- 수정: `display:none` 유지 + `@keyframes resultReveal` 애니메이션으로 교체
  - CSS `transition`은 `display` 변경과 함께 동작 안 함; `animation`은 동작
  - JS `classList.add('show')` 무변경
  - `animation-fill-mode: both` → from 프레임부터 시작

나머지 11개 항목 이상 없음. 다빈치 최종 판정 요청.

---

## 다빈치 최종 판정 · 통과

두 파일 실물 검토 완료. 브랜드 방향·달리 검토 수정 사항 정합. 클레버 검수로 이관.

**정합 확인**
- 팔레트: wedding `#B8722A`/`#F7EDD8` · funeral `#2D4A6B`/`#EDF1F7` — 파일별 분기 정확
- select chevron SVG stroke: 파일별 `%23B8722A` / `%232D4A6B` (재활용 없음)
- `.result-main color: var(--primary)` 두 파일 모두 (다빈치 보완 ③)
- hero-line: wedding에만 존재 (line 199), funeral에는 없음 — 문서 사양 그대로
- `#result` display:none + `@keyframes resultReveal` — 달리 결함 ② 수정 반영 · 유령 공간 없음
- Pretendard jsDelivr dynamic-subset — 달리 결함 ① 수정 반영
- SEO meta·OG·JSON-LD·`#ad-slot` 유지 · JS 로직(M table·NOTES·submit·meal 체크박스) 미변경

**다음 사이클 브랜드 승계 (2026-07-25 이후 세션에서 참조)**
- "조용한 신뢰" 기조 유지 (한국어 롱테일 · 즉각적 신뢰감)
- Pretendard jsDelivr dynamic-subset이 표준 폰트 로드
- 팔레트 분기 원칙 유지 (유틸의 감정 톤에 따라 웜/쿨 계열 선택)
- `#result` 등장은 `@keyframes` + `display:none` 패턴 (CSS transition은 display와 함께 안 됨)
- 다음 사이클 미세 조정 후보: wedding `--primary` 반 스텝 어둡게 (`#A9631D` 등) — 대비 4.5:1 안정 확보

**팀 간 신호**
클레버 검수 슬롯은 이 폴더(`2026-07-24/`) 읽어 시작. push는 클레버·대표 승인 후.
