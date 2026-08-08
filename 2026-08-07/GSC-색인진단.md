# GSC 색인 진단 · 2026-08-08

**세션**: [[자율 지시: webutils-GSC색인]] · 마케팅팀
**실행**: 벤(대리) · **판정 대기**: 제니(팀장)
**날짜**: 2026-08-08 KST
**참조 프롬프트**: `2026-08-07/자율지시-GSC색인-마케팅.md`

---

## 요약

- **사이트 측 결함 3중 동시 발견** — sitemap·robots·canonical 전부 결손 상태. GSC 실 색인 조회 이전에 사이트 측 정합부터 개발팀 결재 상신 필수.
- **가장 심각한 리스크**: 아카이브 폴더(`2026-07-24/`~`2026-08-08/`) 전부 Cloudflare Pages에 웹 노출 상태 · 루트 배포본과 중복 콘텐츠 다중 페어 형성. AdSense 심사 크롤 시 저품질·중복 판정 리스크 매우 큼.
- **GSC 실 색인 조회·개별 URL 색인 요청 · sitemap 재제출은 대표 계정 접근 필요** — AI 대리 실행 불가 · 결재 상신 사안.

---

## 1. sitemap.xml 진단

**결과: 부재**

- HTTP 확인: `https://utils.minon.kr/sitemap.xml` → 200 응답 나오나 **랜딩 HTML 반환** (Cloudflare Pages SPA fallback · 실 sitemap 파일 아님)
- 로컬 확인: 리포 루트에 `sitemap.xml` 파일 없음 · `find /Users/jim/projects/webutils -name "sitemap*"` 매치 0건
- **판정**: 미생성 · GSC 재제출 불가능 · 개발팀 생성 결재 상신 필수

## 2. robots.txt 진단

**결과: 부재**

- HTTP 확인: `https://utils.minon.kr/robots.txt` → 200 응답 나오나 **랜딩 HTML 반환** (SPA fallback · 실 robots 파일 아님)
- 로컬 확인: 리포 루트에 `robots.txt` 파일 없음
- **판정**: 미생성 · 기본값 크롤 허용이나 명시적 robots·sitemap 지시 부재 · AdSense 크롤러 접근 정합 확인 불가 · 개발팀 생성 결재 상신 필수

## 3. ads.txt 진단 (참고)

- **존재 확인 완료**: `/ads.txt` → `google.com, pub-9477150496807643, DIRECT, f08c47fec0942fa0`
- AdSense 신청 완료(8/7)에 맞춘 정합 · 이슈 없음

---

## 4. 색인 대상 17건 사이트 측 정합 표

| # | URL | 로컬 파일 존재 | title | description | canonical | 아카이브 중복 페어 | 정합 판정 |
|---|-----|---|---|---|---|---|---|
| 1 | `utils.minon.kr/` | ✅ | ✅ | ✅ | ✅ (`utils.minon.kr/`) | — | **정합** |
| 2 | `/funeral-condolence-calculator/` | ✅ | ✅ | ✅ | ⚠️ JS 삽입 (line 497) | `2026-07-24/funeral-condolence-calculator/` (canonical 있음) | **JS canonical 리스크** |
| 3 | `/acquisition-tax-calculator/` | ✅ | ✅ | ✅ | ❌ | `2026-07-27/acquisition-tax-calculator/` (canonical 있음) | **canonical 부재 + 중복** |
| 4 | `/ac-electricity-calculator/` | ✅ | ✅ | ✅ | ❌ | `2026-07-25/ac-electricity-calculator/` (canonical 없음) | **canonical 부재 + 중복** |
| 5 | `/studio-electricity-calculator/` | ✅ | ✅ | ✅ | ❌ | `2026-07-25/studio-electricity-calculator/` (canonical 없음) | **canonical 부재 + 중복** |
| 6 | `/real-estate-commission-calculator/` | ✅ | ✅ | ✅ | ❌ | `2026-07-27/real-estate-commission-calculator/` (canonical 있음) | **canonical 부재 + 중복** |
| 7 | `/color-picker/` | ✅ | ✅ | ✅ | ❌ | — | **canonical 부재** |
| 8 | `/national-housing-bond-calculator/` | ✅ | ✅ | ✅ | ❌ | — | **canonical 부재** |
| 9 | `/property-tax-calculator/` | ✅ | ✅ | ✅ | ❌ | — | **canonical 부재** |
| 10 | `/apartment-subscription-score/` | ✅ | ✅ | ✅ | ✅ | `2026-08-01/apartment-subscription-score/` (canonical 있음 → 루트 지목) | **정합 (아카이브가 루트 지목)** |
| 11 | `/apartment-subscription-special/` | ✅ | ✅ | ✅ | ✅ | `2026-08-01/apartment-subscription-special/` (canonical 있음 → 루트 지목) | **정합 (아카이브가 루트 지목)** |
| 12 | `/moving-truck-size-calculator/` | ✅ | ✅ | ✅ | ✅ | `2026-08-03/moving-truck-size-calculator/` (canonical 있음 → 루트 지목) | **정합 (아카이브가 루트 지목)** |
| 13 | `/dorm-vs-rent-calculator/` | ✅ | ✅ | ✅ | ✅ | `2026-08-03/dorm-vs-rent-calculator/` (canonical 있음 → 루트 지목) | **정합 (아카이브가 루트 지목)** |
| 14 | `/resident-registration-deadline/` | ✅ | ✅ | ✅ | ❌ | `2026-08-05/resident-registration-deadline/` (canonical 없음) | **canonical 부재 + 중복** |
| 15 | `/summer-homework-dday-calculator/` | ✅ | ✅ | ✅ | ❌ | `2026-08-05/summer-homework-dday-calculator/` (canonical 없음) | **canonical 부재 + 중복** |
| 16 | `/liberation-day-vacation-planner/` | ✅ | ✅ | ✅ | ❌ | `2026-08-07/liberation-day-vacation-planner/` (canonical 없음) | **canonical 부재 + 중복 · 시류 소멸 임박** |
| 17 | `/weekly-holiday-pay-calculator/` | ✅ | ✅ | ✅ | ❌ | `2026-08-07/weekly-holiday-pay-calculator/` (canonical 없음) | **canonical 부재 + 중복** |

### 결함 집계

- **canonical 부재 (루트 배포)**: 11건 (3·4·5·6·7·8·9·14·15·16·17)
- **JS canonical 삽입 (렌더 의존 리스크)**: 1건 (2 funeral-condolence)
- **아카이브 폴더 웹 노출 중복 콘텐츠 리스크**: 최소 11개 페어 (2026-07-24·2026-07-25×2·2026-07-27×2·2026-08-01×2·2026-08-03×2·2026-08-05×2·2026-08-07×2)
- **아카이브 자체 미정합 (canonical 없이 노출)**: 2026-07-25·2026-08-05·2026-08-07 하위 파일 다수 · canonical 부재로 아카이브가 루트를 지목하지 않음 → GSC가 어느 URL을 정본으로 판단할지 불확실

### 리스크 판정

**심사 대기 중(D-27 · 9/4) AdSense 크롤 시나리오**:
1. sitemap 부재 → 크롤러가 URL 발견 자체 지연·누락 가능
2. 중복 콘텐츠 페어 다수 → 저품질·중복 판정 · **승인 지연 or 승인 후 광고 비활성 리스크**
3. canonical 부재 → 정본 페이지 판별 불가 · 색인 자체 지연

---

## 5. 개발팀 결재 상신 사안 (긴급 · D-27 대응)

**대리 벤 권한 밖 · 개발팀(마이클·클레버) 실행 필요**:

1. **sitemap.xml 생성·배포** — 17개 URL 명시 (루트 + 유틸 16건) · 아카이브 폴더 제외 · Cloudflare Pages 빌드 시 자동 생성 or 정적 파일
2. **robots.txt 생성·배포** — 아카이브 폴더(`2026-*/`) Disallow 명시 · Sitemap 지시 명시 · Googlebot·AdSense 크롤러 접근 명시 허용
3. **canonical 태그 추가 (11건)** — 루트 배포본 각 유틸 index.html에 `<link rel="canonical" href="https://utils.minon.kr/{slug}/">` 삽입
4. **아카이브 폴더 웹 접근 차단 검토** — Cloudflare Pages `_redirects` 또는 폴더 자체 배포 제외 (`.pages-ignore` 등) · 최소 robots.txt Disallow는 즉시 필요
5. **funeral-condolence-calculator JS canonical → static 변경** — 크롤러 렌더 지연 리스크 제거

## 6. 대표 계정 실행 필요 사안 (GSC UI 접근)

**AI 대리 실행 불가 · 대표 직접 실행 or 마이클 결재 승인 후 실행**:

1. **GSC 프로퍼티 등록 상태 확인** — `utils.minon.kr` 도메인 프로퍼티 등록 여부
2. **sitemap.xml 재제출** — 개발팀 sitemap 배포 완료 후 GSC "Sitemaps" 메뉴에서 제출
3. **17건 URL 색인 상태 조회** — GSC "색인 > 페이지" 리포트 · 색인됨/발견됨/색인 안 됨 분류
4. **미색인·색인 지연 페이지 개별 색인 요청** — GSC "URL 검사" 도구 · 지시 우선순위 준수:
   - (1순위) `utils.minon.kr/` 랜딩
   - (2순위) `/liberation-day-vacation-planner/` (8/17 이후 시류 소멸 · 색인 지연 시 완전 손실)
   - (3순위) 나머지 유틸 15건

---

## 7. 벤 판단·권고

- **선행 조건**: sitemap·robots·canonical 결함 미해결 상태에서 GSC 색인 요청은 근본 리스크 잔존. 개발팀 결재 승인·배포 완료 후 GSC 재제출·개별 색인 요청 순서가 정공법.
- **시류 예외**: `liberation-day-vacation-planner`는 8/17 이후 시류 완전 소멸 · **개발팀 배포 대기 없이 대표가 GSC UI에서 즉시 색인 요청 선행** 권고 (canonical 부재 상태여도 색인 자체는 요청 가능 · 정합 미달 잔존 리스크 감수)
- **D-27 시간축**: 개발팀 5건(sitemap·robots·canonical 11건·아카이브 차단·JS→static) 배포 완료 데드라인 **D-14 (2026-08-21)** 권고. 심사 결과 통상 1~4주 · 심사 후반부 크롤 정합 확보 위해 D-14 이전 완료 필수.

---

## 세션 종료 마커 (팀장 제니 발행)

벤 실행 파트 완료 · 제니 판정·마커 발행 대기.
