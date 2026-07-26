# 디자인·검수 노트 · 2026-07-25

## 사전 상태
- 디자인팀 산출 파일 없음 (design-notes.md 부재 → 마이클이 index.html 두 건을 디자인팀 개입 없이 단독 제작)
- 대상 슬러그
  - `ac-electricity-calculator/index.html`
  - `studio-electricity-calculator/index.html`

---

## 클레버 검수

### 4축 검수 결과

- **정확성**: 수정
- **완성도**: 수정
- **원칙**: 수정
- **배포준비**: 조건부 준비

### 수정 항목

**공통 (양 파일)**
1. **브랜드 승계** — 어제(07-24) 사이클에서 확립된 브랜드 팔레트(웜톤 베이지·브라운 CSS 변수 + Pretendard 폰트)를 오늘 두 유틸이 승계하지 않고 시스템 폰트·완전 흑백으로 만들어졌음. 사이트 방문자 관점에서 어제 두 유틸과 다른 사이트로 인식될 위험. 어제 팔레트 그대로 이식 (`--bg #FFFDF8` · `--primary #B8722A` 등).
2. **SEO 완결성** — `<link rel="canonical">` 및 `<meta name="twitter:card">` 계열 부재. 두 파일 모두 추가.
3. **홈 회유 경로** — 상단에 홈 회유 링크 추가. 사이트 정체성 노출 + 다른 유틸로의 회유 경로 확보.

**ac-electricity-calculator 단독**
- 없음 (계산 로직·UX 자체는 견고). 위 공통 3항만 반영.

**studio-electricity-calculator 단독**
4. **냉장고 과대추정 보정** — 정격 소비전력(예: 150W) × 24시간 × 30일 = 108 kWh/월로 계산하면 실제 청구(약 30~50 kWh)의 2~3배로 과대추정. 컴프레서 duty cycle 특성상 실제 평균 소비는 정격의 약 1/3. `FRIDGE_DUTY = 1/3` 계수 도입 + 사용자 안내 문구 추가("컴프레서가 켜졌다 꺼졌다 반복해서 실제 평균 소비는 정격의 약 1/3").
5. **세탁기 W 필드 추가** — 다른 5개 가전은 소비전력 W 편집 가능한데 세탁기만 500W 하드코딩이었음. UX 일관성 위해 W 입력 필드 추가 (기본 500W · 100~2500W).

### 수정 흔적
모든 수정 부위에 `<!-- 클레버 수정: 이유 -->` 인라인 주석 (HTML) 또는 `/* 클레버 수정: 이유 */` (CSS/JS) 표기. 자율지시 원칙 준수.

### 검토했으나 수정하지 않은 것
- **한전 요금 2024년 기준** — 이후 개정 가능성 있으나 disclaimer로 "참고용" 명시. 실시간 요율 반영은 정적 HTML 범위 외.
- **하계 특례 자동 체크** — 지금이 7월이라 default checked 합리적. 사용자가 UI에서 해제 가능.
- **부가세·전력기반기금 계산 순서** — 현재 `Math.round(sub + Math.floor(sub × 0.1) + Math.floor(sub × 0.037))` 방식. 한전 공식(각각 반올림 후 합산·10원 미만 절사)과 미세 차이 있으나 참고용 범위 내 오차.

### 배포 준비 상태
**조건부 준비**

- **조건 1 (필수)**: 브랜드 팔레트가 어제 사이클 것과 정확히 일치하는지 시각 검증 — 클레버가 CSS 변수는 동일하게 이식했으나 실제 렌더링 대조는 배포 후 대표 확인 권장.
- **조건 2 (권장)**: 다음 사이클부터 디자인팀 자율지시(웹유틸-디자인) 산출을 반드시 거친 뒤 개발팀이 착수하도록 파이프라인 강화. 오늘처럼 디자인 산출 없이 개발이 임의 결정하는 경우 브랜드 일관성이 매 사이클 위협받음.

**배포 절차**: 배포 자체는 클레버 자율지시 범위 밖. 사마의 보고 이후 대표 직접 지시로 실행.

### 파일 이동 지시 (배포 시)
- `2026-07-25/ac-electricity-calculator/` → `ac-electricity-calculator/` (프로젝트 루트)
- `2026-07-25/studio-electricity-calculator/` → `studio-electricity-calculator/` (프로젝트 루트)
- 이후 `git add . && git commit -m "add: ac-electricity-calculator, studio-electricity-calculator" && git push origin main`
- Cloudflare Pages 자동 배포 후 `ac-electricity-calculator/` · `studio-electricity-calculator/` 접근 확인

---

*검수 · 개발팀 팀장 클레버 · 2026-07-25*
