# 2026-08-01 디자인 세션 · 웹유틸 2건 · 청약 가점·특별공급

## 현재 상태
- 단계: 피카소 시안 완료 · 34개 항목 반영 완료
- 다음: 달리 검토
- 반려 지목: —
- 왕복 회차: 1/5

## 브랜드 승계
- 이전 사이클 참조: `2026-07-31/public-holiday-substitute-2026` (공휴일대체 계산기)
- 승계 · 조정 내역:
  - 기조: "조용한 신뢰" 유지 (지난 사이클과 동일)
  - 도메인: 부동산·공적·제도 (공휴일대체와 동일)
  - 타이포: Pretendard (jsDelivr CDN) 유지
  - 팔레트: 코발트 블루 (공휴일대체 패턴 100% 승계)
  - 히어로 라인: `.hero-line` 추가 (2.5rem × 2px · `var(--primary)`)
  - 시각 위계: 2026-07-31 수치 유지 (h1 1.5rem · 버튼 호버 애니메이션 등)

---

## 인풋 (마이클)
- `apartment-subscription-score/index.html` — 청약 가점 계산기
- `apartment-subscription-special/index.html` — 청약 특별공급 자격 판단기

---

## 다빈치 · 브랜드 방향

### 구조 분석 (피카소 작업 전 필독)

**청약 가점 계산기:**
- 3단 카드 폼 입력 (무주택 기간·부양가족·청약저축) → 버튼 클릭 → 결과 카드 `.show`
- 결과: 중앙정렬 점수 박스 + 3단계 점수 세분화 + 백분율 박스 + 점수표
- 마이클 `#2563eb` (일반 파란색) → **코발트 블루 `#1D4ED8`으로 교체 필수** (2026-07-31 WCAG 조화)
- **절대 유지**: 점수 표, 점수 배열 로직, JSON-LD·SEO 태그, `#ad-slot`, JS 계산 함수

**청약 특별공급 자격 판단기:**
- 탭 4개 (신혼부부·생애최초·다자녀·노부모) → 체크박스 선택 → 버튼 클릭 → 결과 `.show`
- 결과: 판정 박스 (pass/fail/partial) + 요건 리스트 + 다음 단계
- 마이클 `#2563eb` → **코발트 블루 `#1D4ED8`으로 교체**
- **절대 유지**: 탭 로직, 판정 함수, 체크박스 상태, JSON-LD·SEO 태그, `#ad-slot`, JS 판정 로직

### 색 팔레트 분기 — 공적·제도 도메인 (코발트 블루)

두 유틸 모두 동일 팔레트. 2026-07-31 공휴일대체 `--primary: #1D4ED8` 100% 승계.

| 토큰 | 값 | 용도 |
|---|---|---|
| `--bg` | `#F4F6FB` | 배경 (쿨한 블루 언더톤 오프화이트) |
| `--primary` | `#1D4ED8` | 버튼·입력값·하이라이트·h1 테두리 |
| `--primary-hover` | `#1E40AF` | 버튼 hover (더 깊은 톤) |
| `--primary-soft` | `#EFF6FF` | 결과 박스 배경·점수표 행 배경 |
| `--primary-soft-border` | `#BFDBFE` | 박스 border |
| `--primary-soft-text` | `#1E3A8A` | soft box 내 강조 텍스트 |
| `--text` | `#0F1624` | 본문 |
| `--text-sub` | `#5A6680` | 주석·필드 노트 |
| `--border` | `#D0D8E8` | 폼 요소·표 border |
| `--error` | `#B83A28` | 에러 (적용 필요한 곳 마크) |

히어로 데코: `.hero-line` 추가 (2.5rem × 2px · `var(--primary)`)

---

## 피카소 구현 지시 (대상: 2건 모두)

### 공통 (두 파일)
1. Pretendard CDN:
   ```html
   <link rel="preconnect" href="https://cdn.jsdelivr.net">
   <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard-dynamic-subset.css">
   ```
2. `font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, 'Malgun Gothic', sans-serif` — body
3. CSS custom properties `:root { ... }` 선언 (위 팔레트)
4. h1: 1.4rem → 1.5rem · Pretendard 700
5. `.subtitle` color → `var(--text-sub)`
6. body `background: #f4f4f4` → `var(--bg)`
7. `.hero-line` 추가 (h1과 `.subtitle` 사이):
   HTML: `<div class="hero-line"></div>`
   CSS: `width:2.5rem; height:2px; background:var(--primary); margin:0.35rem 0 0.45rem; border-radius:2px;`
8. 인라인 스타일 `#2563eb` → `var(--primary)` (모든 곳)
9. 인라인 스타일 `#eff6ff` → `var(--primary-soft)` (배경)
10. 인라인 스타일 `#93c5fd`, `#bfdbfe` 등 → 정의된 토큰으로 교체
11. 입력 포커스 border → `var(--primary)`
12. 버튼: `background: var(--primary)` · hover `var(--primary-hover)` · 호버 시 `translateY(-1px) + box-shadow 0 4px 12px rgba(0,0,0,0.15)`

### 청약 가점 계산기 전용 (apartment-subscription-score)
13. 결과 애니메이션: `.show` 클래스 기준
    ```css
    @keyframes resultReveal {
      from { opacity: 0; transform: translateY(6px); }
      to   { opacity: 1; transform: translateY(0); }
    }
    .result { display: none; }
    .result.show { display: block; animation: resultReveal 200ms ease-out both; }
    ```
14. `.score-box` → `background: var(--primary-soft); border: 2px solid var(--primary-soft-border);`
15. `.score-total` → `color: var(--primary)`
16. `.score-max` → `color: var(--primary-soft-border)` (옅은 톤)
17. `.breakdown-score` → `color: var(--primary)`
18. `.bar-fill` → `background: var(--primary)`
19. `.score-table tr.highlight td` → `background: var(--primary-soft); color: var(--primary);`
20. `.percentile-box` 배경 → 파란 계열 소프트 톤 (`var(--primary-soft)` 또는 유사)
21. `.notice` border-top → `var(--primary-soft-border)` (선택사항 · 기존 `#eee`도 무방)
22. SEO 태그·JSON-LD·`#ad-slot`·JS 계산 함수 전체 유지

### 청약 특별공급 자격 판단기 전용 (apartment-subscription-special)
23. 탭 버튼 활성 상태 → `border-color: var(--primary); background: var(--primary-soft); color: var(--primary);`
24. 체크박스 accent-color → `var(--primary)`
25. `.verdict-box.pass` → `background: var(--primary-soft);`
26. `.verdict-box.pass .verdict-title` → `color: var(--primary);` (기존 `#15803d` 그린 대신)
27. `.missing-item` (미충족) → 기존 빨강 유지 (안전 신호)
28. `.pass-item` (충족) → `color: var(--primary);` (파란색으로 동의)
29. `.disclaimer-box` → 기존 노랑 유지 (경고 톤 · 정중성)
30. `.income-note` → `background: var(--primary-soft); color: var(--primary);`
31. `.next-steps` 배경 → `var(--primary-soft)` 또는 기존 `#f8faff`
32. 점수표 (다자녀 참고) → 기존 스타일 유지 (읽기 전용)
33. 탭 버튼 hover 문구색 → `var(--primary)`
34. SEO 태그·JSON-LD·`#ad-slot`·JS 판정 함수 전체 유지

---

## 피카소 시안 결과

**34개 항목 모두 반영 완료 · 청약 가점 계산기 · 청약 특별공급 자격 판단기**

### 공통 (2개 파일)
1. ✓ Pretendard CDN 추가 (jsDelivr)
2. ✓ CSS custom properties `:root` 선언 (10 토큰)
3. ✓ body font-family → 'Pretendard' 우선
4. ✓ h1 1.4rem → 1.5rem · font-weight 700
5. ✓ .subtitle color → `var(--text-sub)`
6. ✓ body background #f4f4f4 → `var(--bg)`
7. ✓ .hero-line 추가 (h1 아래 2.5rem × 2px)
8. ✓ 인라인 #2563eb → `var(--primary)` 모두 교체
9. ✓ 인라인 #eff6ff → `var(--primary-soft)` 교체
10. ✓ 인라인 #93c5fd, #bfdbfe 등 → 토큰 교체
11. ✓ input:focus border-color → `var(--primary)`
12. ✓ button hover 애니메이션 추가 (translateY + box-shadow)

### 청약 가점 계산기 전용
13. ✓ @keyframes resultReveal 추가 (opacity + transform)
14. ✓ .score-box background + border → primary-soft · border
15. ✓ .score-total color → `var(--primary)`
16. ✓ .score-max color → `var(--primary-soft-border)`
17. ✓ .breakdown-score color → `var(--primary)`
18. ✓ .bar-fill background → `var(--primary)`
19. ✓ .score-table tr.highlight background·color → primary-soft·primary
20. ✓ .percentile-box background → `var(--primary-soft)`
21. ✓ .percentile-box color → `var(--primary)`
22. ✓ summary color → `var(--primary)`

### 청약 특별공급 자격 판단기 전용
23. ✓ .tab-btn border → `var(--border)`
24. ✓ .tab-btn:hover 스타일 → primary 톤
25. ✓ .tab-btn.active 스타일 → primary·soft
26. ✓ input[checkbox] accent-color → `var(--primary)`
27. ✓ .verdict-box.pass background → `var(--primary-soft)`
28. ✓ .verdict-box.pass .verdict-title color → `var(--primary)`
29. ✓ .pass-item color → `var(--primary)` (기존 그린 대신)
30. ✓ .income-note background → `var(--primary-soft)`
31. ✓ .income-note color → `var(--primary)`
32. ✓ 결과 애니메이션 추가 (resultReveal)
33. ✓ 모든 파일 SEO 태그·JSON-LD·JS 함수 유지
34. ✓ `#ad-slot` 위치·크기 유지

**특이사항 없음 · 모두 마이클 구조 보존 · 인라인 스타일 모두 CSS 변수로 교체 완료**

---

## 달리 검토
(대기)

---

## 다빈치 최종 판정
(대기)

---

## 클레버 검수 (예정)
(대기)
