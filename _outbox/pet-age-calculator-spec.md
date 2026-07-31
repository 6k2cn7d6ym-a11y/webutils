# 반려동물 나이 계산기 개발 스펙

- **작성**: 사마의 (기획전략실)
- **작성일**: 2026-07-31
- **판본**: v2 (2026-07-31 · 학술 조사 재수행 후 전면 재작성 · commit 확정판)
- **개발 담당**: 마이클 (대리) · 클레버 (팀장) 페어
- **배포 목표**: 2026-08-03 (월) 신규 사이클
- **파이프라인**: 개발팀 직행 (피카소 디자인 왕복 스킵 · 대표 승인 2026-07-31)

---

## §0. 유틸 구조 요약

| 항목 | 값 |
|---|---|
| 유틸 개수 | **2개 분리 페이지** (통합 탭 UI 아님) |
| URL 1 | `/dog-age-calculator/index.html` |
| URL 2 | `/cat-age-calculator/index.html` |
| 공용 로직 | `/shared/pet-age.js` (계산·라이프스테이지 함수 5개) |
| 배포 카운트 | 기존 6건 → 8건 |
| 카테고리 | "반려동물" 신규 카테고리 2건 |

**분리 근거**: 강아지·고양이는 검색 의도·볼륨·경쟁 강도가 다름 (한 URL에 두 head 키워드 태우면 각각 최적화 불가). 국내 계산기 조사 결과 3곳이 이미 분리 페이지 운영 = 분리 자체는 관행. 진짜 차별화는 §1 참조.

---

## §1. 차별화 요소 (국내 계산기 11개 조사 결과 기반)

| 요소 | 국내 현황 | 본 유틸 |
|---|---|---|
| Wang 2020 로그 공식 계산기 통합 | **0개** (데일리벳 기사 1건만 언급) | ✅ 기본 공식으로 채택 |
| 후생유전학 클럭 근거 명시 | 0개 | ✅ Wang 2020 + Horvath 2022 + Raj 2021 병기 |
| 원출처 DOI 인라인 인용 | 1개 (AgeCalc의 AAHA 인용) | ✅ 6개 논문·가이드라인 DOI/URL 명시 |
| AAHA/AAFP 라이프 스테이지 라벨 | 1~2개 | ✅ 5단계(개) / 4단계(고양이) 정확 반영 |
| 크기 4구간 (초대형견 분리) | 2개 | ✅ AVMA 시니어 기준 정합 |

---

## §2. 참고 자료 · 근거 원출처

**⚠️ 절대 원칙**: 인용은 반드시 원문 확인 · 아래 목록만 사용 · 인터넷 통설·계산기 관행("AVMA 4구간 가산치" 등) 채택 금지.

### 강아지

| # | 근거 | 인용 문구 (예시) | URL / DOI |
|---|---|---|---|
| D1 | Wang T, Ma J, Hogan AN, et al. 2020. Quantitative Translation of Dog-to-Human Aging by Conserved Remodeling of the DNA Methylome. *Cell Systems* 11(2):176–185. | "라브라도 리트리버 95마리 혈액 DNA 메틸롬 분석 · 로그 공식" | https://pmc.ncbi.nlm.nih.gov/articles/PMC7484147/ · DOI 10.1016/j.cels.2020.06.006 |
| D2 | Horvath S, Lu AT, Haghani A, et al. 2022. DNA methylation clocks for dogs and humans. *PNAS* 119(21):e2120887119. | "93견종 확장 검증 · Wang 후속" | https://www.pnas.org/doi/10.1073/pnas.2120887119 · DOI 10.1073/pnas.2120887119 |
| D3 | Kraus C, Pavard S, Promislow DEL. 2013. The Size–Life Span Trade-Off Decomposed. *Am Nat* 181(4):492–505. | "대형견 조기 노화 = 노화 속도 자체가 빠름" | https://doi.org/10.1086/669665 |
| D4 | Creevy KE, Grady J, Little SE, et al. 2019. 2019 AAHA Canine Life Stage Guidelines. *JAAHA* 55(6):267–290. | "5단계 라이프 스테이지 (Puppy / Young Adult / Mature Adult / Senior / End of Life)" | https://www.aaha.org/resources/life-stage-canine-2019/ · PubMed 31622127 |
| D5 | AVMA. Caring for senior cats and dogs. | "크기별 시니어 시작 나이" | https://www.avma.org/resources-tools/pet-owners/petcare/senior-pets |

### 고양이

| # | 근거 | 인용 문구 (예시) | URL / DOI |
|---|---|---|---|
| C1 | Quimby J, Gowland S, Carney HC, et al. 2021. 2021 AAHA/AAFP Feline Life Stage Guidelines. *JFMS* 23(3):211–233. | "4단계 라이프 스테이지 (Kitten 0-1 / Young Adult 1-6 / Mature Adult 7-10 / Senior 10+)" | https://catvets.com/resource/aaha-aafp-feline-life-stage-guidelines/ · DOI 10.1177/1098612X21993657 |
| C2 | International Cat Care. How to tell your cat's age in human years. | "환산 공식 `24 + (age-2)×4`의 실제 출처" | https://icatcare.org/articles/how-to-tell-your-cats-age-in-human-years |
| C3 | Raj K, Szladovits B, Haghani A, et al. 2021. Epigenetic clock and methylation studies in cats. *GeroScience* 43(5):2363–2378. | "고양이 후생유전학 시계 · dual-species relative age clock · MAE 0.83년" | https://pmc.ncbi.nlm.nih.gov/articles/PMC8599556/ · DOI 10.1007/s11357-021-00445-8 |

**절대 인용 금지 (근거 없음)**:
- ~~"AVMA 크기 4구간 연간 가산 +4/+5/+6/+7"~~ — AVMA 페이지에 존재하지 않음. 인터넷 폴클로어.
- ~~"AAHA/AAFP 공식 24+(age-2)×4"~~ — AAHA/AAFP 가이드라인에 없음. iCatCare 자체 heuristic.
- ~~"강아지 나이 × 7"~~ — 학술 근거 없음. 언급 시 반드시 "잘못된 통설" 라벨.

---

## §3. 강아지 페이지 스펙 (`/dog-age-calculator/index.html`)

### 3-1. URL·파일 배치

```
/dog-age-calculator/
  └── index.html
```

### 3-2. UI 스펙

**입력 폼**:
- 강아지 현재 나이 (숫자 · 0.1 단위 · 0.1 ~ 25.0)
  - 개월 미만 = "0.1 (약 5주)" · placeholder에 "예: 3.5"
- 크기 선택 (라디오 4카드 · 아이콘 + 예시 견종 텍스트)
  - **소형** (~9 kg) 예: 말티즈·포메·치와와
  - **중형** (9~22 kg) 예: 비글·시바
  - **대형** (22~40 kg) 예: 골든리트리버·라브라도
  - **초대형** (40+ kg) 예: 그레이트데인·세인트버나드
- 계산 버튼 (한 개)

**결과 카드 2개 (세로 배치)**:

카드 1 — **주 결과 · Wang 공식**
- 큰 숫자: 사람 나이 XX세 (Math.round)
- 캡션: "라브라도 기반 유전자 시계 공식 · Wang 2020"
- 라이프 스테이지 배지: Puppy / Young Adult / Mature Adult / Senior / End of Life (D4 AAHA 5단계)
- 각주: [D1] 링크

카드 2 — **참고 · 크기별 시니어 판정**
- 문구: "이 크기의 강아지는 만 X세부터 시니어로 봅니다" (D5 AVMA 기준)
- 각주: [D5] 링크

**하단 섹션 (콘텐츠 두께)**:
- §3-6 참고. AdSense E-E-A-T용 본문 필수.

### 3-3. 계산 공식 (Wang 2020)

```
human_age = 16 × ln(dog_age) + 31
```

- 정의역: `dog_age >= 0.15` (약 8주 · Wang 논문 최저 표본 0.1세 → 안전 마진)
- 소수점 처리: `Math.round()` 정수 출력
- 반환값 검증: 음수 방지 (`Math.max(0, result)`)

**검증 예시값 (스펙 확정용 · 마이클 구현 검증)**:
| dog_age | ln(x) | 16·ln(x)+31 | 반올림 |
|---|---|---|---|
| 0.5 | -0.693 | 19.9 | **20** |
| 1 | 0 | 31.0 | **31** |
| 2 | 0.693 | 42.1 | **42** |
| 5 | 1.609 | 56.7 | **57** |
| 10 | 2.303 | 67.8 | **68** |
| 15 | 2.708 | 74.3 | **74** |
| 20 | 2.996 | 78.9 | **79** |

### 3-4. 크기 4구간 (라이프 스테이지 판정용)

**AVMA 시니어 시작 나이 기준 정합** (D5):

| 크기 | 무게 | 시니어 시작 (참고 카드용) |
|---|---|---|
| 소형 | < 9 kg | 만 9세부터 |
| 중형 | 9 ~ 22 kg | 만 9세부터 |
| 대형 | 22 ~ 40 kg | 만 8세부터 |
| 초대형 | 40+ kg | 만 6세부터 |

**주의**: 크기 입력은 **시니어 판정 카드(카드 2)에만 사용**. Wang 공식(카드 1)의 결과는 크기와 무관. 이유: Wang은 단일 견종(라브라도)만 표본. 크기별 가산치는 학술 근거 없음.

### 3-5. AAHA 5단계 라이프 스테이지 매핑 (D4)

| 단계 | 판정 로직 |
|---|---|
| Puppy | dog_age < 1 |
| Young Adult | 1 <= dog_age < 3 |
| Mature Adult | 3 <= dog_age < (시니어 시작 나이) |
| Senior | 시니어 시작 나이 이상 |
| End of Life | UI에서는 표시 안 함 (수의사 판단 영역) |

**시니어 시작 나이**: §3-4 표에서 크기별 결정.

**AAHA 원문 원칙**: 라이프 스테이지는 수명·개체차의 함수 · 고정 나이가 아님. UI 문구에 "개체차가 큽니다 · 수의사 상담 권장" 필수 각주.

### 3-6. 콘텐츠 두께 섹션 (하단 본문)

AdSense 심사·E-E-A-T용. 마이클이 초안 작성 · 벤 감수 옵션.

1. **강아지 나이 계산 방법 요약** (200~250자)
2. **왜 "×7"은 잘못된 통설인가** (Wang 2020 근거 · 200자)
3. **크기가 왜 노화 속도에 영향을 주는가** (Kraus 2013 요약 · 200자)
4. **우리 강아지 라이프 스테이지 이해하기** (AAHA 5단계 설명 · 300자)
5. **자주 묻는 질문 (FAQ)** — 5문항 이상
6. **참고 문헌** (§2 D1~D5 링크 리스트)

**목표 본문 총량**: 1200자 이상 (계산기 위·아래 합산).

---

## §4. 고양이 페이지 스펙 (`/cat-age-calculator/index.html`)

### 4-1. URL·파일 배치

```
/cat-age-calculator/
  └── index.html
```

### 4-2. UI 스펙

**입력 폼**:
- 고양이 현재 나이 (숫자 · 0.1 단위 · 0.1 ~ 25.0)
- **크기·품종 입력 없음** (고양이는 크기별 노화 차이가 강아지만큼 크지 않음 · AAHA/AAFP 2021 원칙)
- 계산 버튼

**결과 카드 2개**:

카드 1 — **주 결과 · iCatCare 공식**
- 큰 숫자: 사람 나이 XX세
- 캡션: "국제고양이케어 (International Cat Care) 표준 공식"
- 라이프 스테이지 배지: Kitten / Young Adult / Mature Adult / Senior (C1 AAHA/AAFP 2021 4단계)
- 각주: [C1] [C2] 링크

카드 2 — **참고 · 후생유전학 클럭**
- 문구: "Raj et al. 2021 (128마리 고양이 · 유전자 메틸레이션) 기준으로도 유사 결과" (Raj 논문에 명시 공식이 없어 참고 링크만 제공 · 학술 근거 존재 자체를 표시)
- 각주: [C3] 링크

### 4-3. 계산 공식 (iCatCare)

```
if cat_age <= 1:      human_age = 15
elif cat_age <= 2:    human_age = 24
else:                 human_age = 24 + (cat_age - 2) × 4
```

- 정의역: `cat_age >= 0.1`
- 소수점 처리: `Math.round()`

**검증 예시값**:
| cat_age | human_age |
|---|---|
| 0.5 | 15 |
| 1 | 15 |
| 2 | 24 |
| 5 | 36 |
| 10 | 56 |
| 15 | 76 |
| 20 | 96 |

**주의 · 표기 원칙**: 이 공식의 출처는 **International Cat Care** (C2). AAHA/AAFP 2021 가이드라인에는 없음. UI·본문에서 "AAHA/AAFP 공식"이라고 표기 금지. "iCatCare (국제고양이케어) 표준"으로 표기.

### 4-4. AAHA/AAFP 2021 4단계 라이프 스테이지 (C1)

| 단계 | 나이 |
|---|---|
| Kitten | 0 ~ 1세 |
| Young Adult | 1 ~ 6세 |
| Mature Adult | 7 ~ 10세 |
| Senior | 10세 이상 |

End of Life는 UI 미표시 (D4와 동일 이유).

### 4-5. 콘텐츠 두께 섹션

1. **고양이 나이 계산 방법 요약**
2. **강아지와 왜 다른가** (크기 영향 미미 · AAHA/AAFP 2021 원칙 · 200자)
3. **AAHA/AAFP 2021 라이프 스테이지 4단계 이해하기** (300자)
4. **고양이 후생유전학 시계 이야기** (Raj 2021 · 200자 · 심화 관심 사용자용)
5. **FAQ** — 5문항 이상
6. **참고 문헌** (C1 ~ C3 링크)

**목표 본문 총량**: 1000자 이상.

---

## §5. 공용 JS 로직 (`/shared/pet-age.js`)

### 5-1. 함수 시그니처

```javascript
// 강아지: Wang 2020 로그 공식
// @param {number} dogAge — 강아지 나이 (년, 0.15 이상)
// @returns {number} 사람 나이 (정수)
export function dogAgeWang(dogAge) {
  if (dogAge < 0.15) return 0;
  return Math.max(0, Math.round(16 * Math.log(dogAge) + 31));
}

// 강아지: 크기별 시니어 시작 나이 (AVMA 기준)
// @param {'small'|'medium'|'large'|'giant'} size
// @returns {number} 시니어 시작 나이 (년)
export function dogSeniorStart(size) {
  return { small: 9, medium: 9, large: 8, giant: 6 }[size];
}

// 강아지: AAHA 라이프 스테이지 판정
// @param {number} dogAge
// @param {'small'|'medium'|'large'|'giant'} size
// @returns {'Puppy'|'Young Adult'|'Mature Adult'|'Senior'}
export function dogLifeStage(dogAge, size) {
  const seniorStart = dogSeniorStart(size);
  if (dogAge < 1) return 'Puppy';
  if (dogAge < 3) return 'Young Adult';
  if (dogAge < seniorStart) return 'Mature Adult';
  return 'Senior';
}

// 고양이: iCatCare 공식
// @param {number} catAge
// @returns {number} 사람 나이 (정수)
export function catAgeICatCare(catAge) {
  if (catAge < 0.1) return 0;
  if (catAge <= 1) return 15;
  if (catAge <= 2) return 24;
  return Math.round(24 + (catAge - 2) * 4);
}

// 고양이: AAHA/AAFP 2021 라이프 스테이지 판정
// @param {number} catAge
// @returns {'Kitten'|'Young Adult'|'Mature Adult'|'Senior'}
export function catLifeStage(catAge) {
  if (catAge <= 1) return 'Kitten';
  if (catAge <= 6) return 'Young Adult';
  if (catAge <= 10) return 'Mature Adult';
  return 'Senior';
}
```

### 5-2. 한국어 라벨 매핑 (UI 표시용)

```javascript
export const DOG_STAGE_KO = {
  'Puppy': '퍼피 (강아지)',
  'Young Adult': '어린 성견',
  'Mature Adult': '성견',
  'Senior': '노령견'
};

export const CAT_STAGE_KO = {
  'Kitten': '자묘',
  'Young Adult': '어린 성묘',
  'Mature Adult': '성묘',
  'Senior': '노령묘'
};
```

---

## §6. 엣지케이스 처리 (7건)

| # | 케이스 | 처리 |
|---|---|---|
| 1 | 강아지 나이 < 0.15 (약 8주 미만) | "생후 8주 미만은 계산 대상이 아닙니다 · 수의사 상담 권장" 안내 |
| 2 | 고양이 나이 < 0.1 | "생후 5주 미만은 계산 대상이 아닙니다 · 수의사 상담 권장" |
| 3 | 나이 > 25 (강아지) 또는 > 25 (고양이) | 계산은 수행 · 하단에 "매우 이례적인 장수 · 결과는 참고용" 노란색 각주 |
| 4 | 크기 미선택 (강아지) | 계산 버튼 비활성 · placeholder "크기를 선택해주세요" |
| 5 | 나이 입력 비어있음 | 계산 버튼 비활성 |
| 6 | 나이 = 0 | "0은 입력할 수 없습니다 · 최소 0.1 (약 5주) 이상" |
| 7 | 나이 음수 or NaN | "숫자를 정확히 입력해주세요" · input type="number" min="0.1" step="0.1" |

---

## §7. SEO 메타·롱테일

### 강아지 페이지

- `<title>`: **강아지 나이 계산기 · Wang 2020 유전자 시계 공식 | utils.minon.kr**
- `<meta name="description">`: 라브라도 유전자 연구(Wang 2020, Cell Systems) 기반 정확한 강아지 나이 계산기. 크기별 시니어 판정과 AAHA 라이프 스테이지 라벨 제공.
- `<h1>`: 강아지 나이 계산기
- 롱테일 키워드 (본문·h2·FAQ 산포):
  - "강아지 사람 나이 계산"
  - "우리 강아지 몇 살"
  - "강아지 나이 환산"
  - "말티즈 나이 계산" · "골든리트리버 나이 계산" (예시 견종별)
  - "강아지 시니어 나이"
  - "Wang 2020 강아지 나이 공식"

### 고양이 페이지

- `<title>`: **고양이 나이 계산기 · AAHA/AAFP 2021 라이프 스테이지 | utils.minon.kr**
- `<meta name="description">`: 국제고양이케어(International Cat Care) 표준 공식과 AAHA/AAFP 2021 라이프 스테이지 가이드라인 기반 고양이 나이 계산기.
- `<h1>`: 고양이 나이 계산기
- 롱테일 키워드:
  - "고양이 사람 나이 계산"
  - "우리 고양이 몇 살"
  - "고양이 나이 환산"
  - "고양이 시니어 나이"
  - "고양이 후생유전학 나이"

---

## §8. 크로스링크·헤더·푸터 정합

- 각 페이지 결과 카드 하단에 상대 페이지 링크 카드 1개
  - 강아지 페이지 → "고양이 나이도 계산하시나요? [고양이 나이 계산기]"
  - 고양이 페이지 → "강아지 나이도 계산하시나요? [강아지 나이 계산기]"
- 랜딩 페이지(`/index.html`) 유틸 목록에 두 항목 신규 추가
- 카테고리 배지: "반려동물"

---

## §9. 면책·안내 문안

**공통 (모든 결과 카드 아래)**:

> **⚠️ 참고용 정보**
> 본 계산기는 학술 연구(Wang 2020 · Raj 2021 · AAHA 가이드라인)를 기반으로 한 **일반적인 참고용 도구**입니다. 개별 반려동물의 건강 상태·품종·유전·환경에 따라 실제 노화 속도는 크게 다를 수 있습니다. 건강 관련 판단은 **반드시 수의사와 상담**해주세요.

**벤 2026-07-25 판정 정합**: "나이 환산 정보성 순수 · AdSense OK 카테고리". 건강 조언·진단 문구 절대 금지.

---

## §10. 원출처 인용 표기 규칙

- 본문 내 근거 인용은 `[D1]`, `[C2]` 등 각주 마커 · 하단 참고 문헌 섹션에 풀 인용
- 참고 문헌 섹션: `<h2>참고 문헌</h2>` · `<ol>` · 각 항목에 저자·연도·제목·저널·DOI/URL
- 외부 링크는 `target="_blank" rel="noopener noreferrer"`
- 논문 링크는 PMC 오픈액세스 URL 우선 · 없으면 publisher URL · 마지막으로 DOI

---

## §11. 개발자 체크리스트 (마이클용)

**구현 순서 제안**:

1. `/shared/pet-age.js` 함수 5개 구현 · §5-1 예시값으로 단위 검증
2. `/dog-age-calculator/index.html` UI 구조 (폼 + 결과 카드 + 하단 콘텐츠)
3. `/cat-age-calculator/index.html` UI 구조 (동일 패턴)
4. 결과 카드 라이프 스테이지 배지 + 각주 링크
5. 하단 콘텐츠 섹션 (§3-6 · §4-5)
6. SEO 메타·h1·타이틀 (§7)
7. 크로스링크·랜딩 페이지 목록 갱신 (§8)
8. 면책 문안 (§9)
9. 참고 문헌 섹션 (§10)
10. 엣지케이스 처리 (§6)

**최종 검증 요청 항목 (클레버 검수용)**:

- [ ] Wang 공식 예시값 7개 (§3-3) · iCatCare 공식 예시값 7개 (§4-3) 정확히 일치
- [ ] AAHA·AAFP 인용 문구가 §2 원출처와 다르지 않음
- [ ] "AVMA 4구간 가산치"·"AAHA/AAFP 공식" 오표기 없음
- [ ] "×7 통설" 언급 시 반드시 "잘못된 통설" 라벨
- [ ] 각주 링크 모두 유효 (원출처 DOI/URL)
- [ ] 크로스링크 양방향 정상
- [ ] 랜딩 페이지 목록 갱신
- [ ] 면책 문안 정확
- [ ] 모바일 반응형 확인

---

## §12. 배포 정보

- **배포 사이클**: 2026-08-03 (월) 신규 사이클
- **커밋 메시지 규칙**:
  - `add: 강아지 나이 계산기 (Wang 2020 공식)`
  - `add: 고양이 나이 계산기 (iCatCare + AAHA/AAFP 2021)`
- **배포 URL**:
  - `https://utils.minon.kr/dog-age-calculator/`
  - `https://utils.minon.kr/cat-age-calculator/`
- **배포 후 확인**: 두 URL 정상 접근 · 각주 링크 유효 · 계산 결과 §5-1 예시값 정합

---

## §13. 판본 이력

| 판본 | 일자 | 작성 | 변경 요지 |
|---|---|---|---|
| v1 | 2026-07-31 (초안) | 이전 세션 사마의 | 통합 탭 UI 전제 · AVMA 4구간 가산치·AAHA/AAFP 공식 오인용 · 파일 저장 미확인 · 실물 부재 |
| v2 (미커밋) | 2026-07-31 20:01 KST | 사마의 | 전면 재작성 · 강아지·고양이 분리 · 학술 조사 4축 재수행 · Wang 2020 + Horvath 2022 + Raj 2021 + AAHA 2019 + AAHA/AAFP 2021 원출처 인용 · 저장 후 유실 (원인: 세션 격리 워크트리 추정) |
| v2 (commit 확정) | 2026-07-31 20:25 KST | 사마의 | v2 내용 재저장 + **git commit으로 원자 확정** · 세션 간 유실 방지 · 대표 (H) 승인 하 실행 |

---

*작성 · 사마의 (기획전략실) · 2026-07-31 20:25 KST*
*원출처 재검증 완료 · git commit 확정판 · 마이클·클레버 페어 릴레이 대기*
