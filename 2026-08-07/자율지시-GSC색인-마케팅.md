# [[자율 지시: 웹유틸-GSC색인-마케팅]]

**개시**: 사마의 (기획전략실 팀장 · 대표 명시 위임 하 · 2026-08-07 13:40 KST)
**대상**: 마케팅팀 · 벤(대리) 실행 · 제니(팀장) 판정
**전제**: AdSense 승인 통과 · 광고 활성화 = 색인된 페이지만 수익 · 미색인 = 수익 0

---

## 할 것

### 1. sitemap.xml 검증·재제출
- Cloudflare Pages 배포 후 sitemap.xml 현행 상태 확인 (없으면 개발팀 결재 상신)
- Google Search Console(GSC)에서 `https://utils.minon.kr/sitemap.xml` 재제출

### 2. 16건 유틸 색인 상태 전수 진단
- GSC "색인 > 페이지" 리포트에서 다음 16건 상태 확인:
  - funeral-condolence-calculator · acquisition-tax-calculator · ac-electricity-calculator · studio-electricity-calculator · real-estate-commission-calculator · color-picker · national-housing-bond-calculator · property-tax-calculator
  - apartment-subscription-score · apartment-subscription-special · moving-truck-size-calculator · dorm-vs-rent-calculator
  - resident-registration-deadline · summer-homework-dday-calculator · liberation-day-vacation-planner · weekly-holiday-pay-calculator
- 상태 분류: 색인됨 · 색인 요청 대기 · 발견됨(색인 안 됨) · 색인되지 않음
- 미색인 사유 파악 (robots.txt·noindex·canonical 문제·중복 콘텐츠 등)

### 3. 미색인·색인 지연 페이지 개별 색인 요청
- GSC "URL 검사" 도구에서 개별 페이지 색인 요청 (16건 각 URL)
- 시류 유틸(liberation-day-vacation-planner · 8/17 이후 소멸) 우선 처리

### 4. robots.txt 상태 확인
- `https://utils.minon.kr/robots.txt` 200 응답 확인 (없으면 개발팀 결재 상신)
- Disallow 규칙 검토 · Googlebot·AdSense 크롤러 접근 100% 보장

### 5. 산출물 저장
- `webutils/2026-08-07/GSC-색인진단.md`
- 16건 색인 상태 표 + 재제출·색인 요청 결과 + robots·sitemap 정합 진단

## 세션 종료 마커 (팀장 제니)
- 완료: `[[기록: 완료 | GSC sitemap 재제출 · 16건 색인 상태 전수 진단 · 미색인 N건 색인 요청 · robots·sitemap 정합 확인]]` → `[[자율종결]]`
