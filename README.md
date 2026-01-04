# 🎯 Algorithm Mastery - PCCP 합격을 위한 105일 프로젝트

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2F[YOUR_USERNAME]%2Falgorithm-mastery&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=visitors&edge_flat=false)](https://hits.seeyoufarm.com)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white)
![Java](https://img.shields.io/badge/Java-007396?style=flat-square&logo=Java&logoColor=white)

> **"안 될 것 같았던 목표를, 어느 세월에 이루나 싶던 꿈을 현실로 만드는 과학적 접근"**

## 📌 프로젝트 개요

**목표**: 개발자 부트캠프/대학원 합격을 위한 체계적인 알고리즘 문제 해결 역량 구축  
**기간**: 2026.01.04 (토) ~ 2026.04.19 (토) - 총 105일  
**핵심 전략**: 역방향 목표 설정(Reverse Engineering) + 80/20 법칙

### 🎓 3단계 연속 인증 목표

| 단계 | 목표 | 인증 날짜 | D-Day | 주요 학습 내용 |
|:---:|:---|:---:|:---:|:---|
| 1️⃣ | **PCCP Level 2 (Python)** | 2026.02.22 | D-49 | Level 1-2 마스터, 핵심 알고리즘 패턴 |
| 2️⃣ | **PCCP Level 3 (Python)** | 2026.03.15 | D-70 | Level 3 돌파, 고급 알고리즘 심화 |
| 3️⃣ | **PCCP Level 2 (Java)** | 2026.04.19 | D-105 | 이중 언어 구사, Java 전환 완료 |

---

## 📊 현재 진행 상황

### 🔥 연속 학습 기록
![GitHub Streak](https://github-readme-streak-stats.herokuapp.com/?user=[0cars0903]&theme=dark)

### 📈 주차별 누적 통계 (2026년 기준)

| 주차 | 기간 | Level 1 | Level 2 | Level 3 | 총 문제 수 | 누적 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Week 1 | 01/04-01/10 | 40 | 0 | 0 | 40 | 40 |
| Week 2 | 01/11-01/17 | - | 10 | 0 | 10 | 50 |
| Week 3 | 01/18-01/24 | - | 10 | 0 | 10 | 60 |
| Week 4 | 01/25-01/31 | - | 15 | 0 | 15 | 75 |
| **진행 중** | - | **0** | **0** | **0** | **0** | **0** |

> 💡 **현재 목표**: Week 1 - Level 1 마스터 40문제 돌파 (진행률: 0%)

---

## 🗂️ 리포지토리 구조

```
algorithm-mastery/
├── README.md                    # 이 파일 (프로젝트 대시보드)
├── .gitignore                   # Python/Java 빌드 산출물 제외
├── COMMIT_GUIDE.md              # 커밋 컨벤션 가이드
├── PROBLEM_SOLVING_LOG.md       # 일일 문제 풀이 로그
│
├── docs/                        # 📚 알고리즘 이론 정리
│   ├── data-structures/         # 자료구조 개념 정리
│   │   ├── stack-queue.md
│   │   ├── hash-map.md
│   │   ├── heap-priority-queue.md
│   │   └── tree-graph.md
│   ├── algorithms/              # 알고리즘 개념 정리
│   │   ├── sorting.md
│   │   ├── dfs-bfs.md
│   │   ├── dynamic-programming.md
│   │   ├── greedy.md
│   │   └── binary-search.md
│   └── syntax-mapping/          # Python-Java 문법 매핑
│       └── python-java-cheatsheet.md
│
├── src/                         # 💻 소스 코드 메인 디렉토리
│   ├── programmers/             # 프로그래머스 문제 풀이
│   │   ├── level1/
│   │   │   ├── solved/          # ✅ 해결 완료 문제
│   │   │   │   ├── p42576_완주하지_못한_선수.py
│   │   │   │   └── p42576_완주하지_못한_선수.java
│   │   │   └── failed/          # ❌ 미해결 문제 (재도전 필요)
│   │   │       └── p12345_어려운_문제_retry.py
│   │   ├── level2/
│   │   │   ├── solved/
│   │   │   └── failed/
│   │   └── level3/
│   │       ├── solved/
│   │       └── failed/
│   │
│   ├── baekjoon/                # 백준 문제 풀이
│   │   ├── silver/
│   │   └── gold/
│   │
│   └── pccp/                    # 🏆 PCCP 모의고사 전용
│       ├── mock-exam-1/
│       ├── mock-exam-2/
│       └── final-prep/
│
└── tests/                       # ✅ 테스트 케이스 (선택)
    └── test_solutions.py
```

---

## 📝 문제 풀이 프로세스

### ✅ 성공적으로 문제를 해결한 경우

#### 1단계: 문제 풀이
```bash
# 프로그래머스 Level 1 문제 풀이 중...
# src/programmers/level1/solved/ 디렉토리에 파일 생성
```

#### 2단계: 파일 저장 규칙
```
파일명 형식: p{문제번호}_{문제이름}.{확장자}

예시:
✅ p42576_완주하지_못한_선수.py
✅ p42748_K번째수.py
✅ p42840_모의고사.java
```

#### 3단계: Git 커밋 (Semantic Commit)
```bash
# 1. 스테이징
git add src/programmers/level1/solved/p42576_완주하지_못한_선수.py

# 2. 커밋 (반드시 아래 형식 준수)
git commit -m "feat(level1): solve '완주하지 못한 선수' using hash map

- Algorithm: Hash (Dictionary)
- Time Complexity: O(N)
- Key Idea: collections.Counter()를 활용한 빈도 비교
- Solved in: 15분"

# 3. 푸시
git push origin main
```

#### 4단계: Notion 기록
- **문제 데이터베이스**에 새 페이지 추가
  - 풀이 상태: `해결(Solved)` ✅
  - 소요 시간: 15분
  - 체감 난이도: 하
  - 핵심 알고리즘: Hash

---

### ❌ 문제를 해결하지 못한 경우

#### 1단계: 실패 파일 저장
```bash
# failed/ 디렉토리에 저장 (시도한 코드 보존)
src/programmers/level1/failed/p12345_어려운_문제_attempt1.py
```

#### 2단계: Git 커밋 (실패도 기록한다!)
```bash
git add src/programmers/level1/failed/p12345_어려운_문제_attempt1.py

git commit -m "attempt(level1): failed to solve '어려운 문제' - need review

- Attempted Approach: 완전탐색으로 시도했으나 시간 초과
- Blocker: O(N^3) 복잡도 문제
- Next Action: 이진 탐색 개념 학습 후 재도전
- Time Spent: 40분"

git push origin main
```

#### 3단계: 타인의 풀이 학습
```bash
# 모범 답안을 참고한 후 새 파일 생성
src/programmers/level1/solved/p12345_어려운_문제_solution.py
```

#### 4단계: 리팩토링 커밋
```bash
git add src/programmers/level1/solved/p12345_어려운_문제_solution.py

git commit -m "refactor(level1): solve '어려운 문제' after learning binary search

- Reference: 프로그래머스 다른 사람 풀이 참고
- Key Insight: 정렬 후 이진 탐색 적용으로 O(N log N) 달성
- Learned: bisect 모듈 활용법
- Original Attempt: see failed/ directory"

git push origin main
```

#### 5단계: Notion 오답 노트 작성
- **회고 템플릿** 작성
  - 문제 정의: "최소값을 찾는 문제였으나..."
  - 실패 원인: "완전탐색의 시간 복잡도 계산 실수"
  - 해결의 열쇠: "이진 탐색 개념"
  - 액션 아이템: "이진 탐색 관련 문제 3개 더 풀기"

---

## 🎨 커밋 메시지 컨벤션

모든 커밋은 **Conventional Commits** 형식을 따릅니다.

### 기본 형식
```
<type>(<scope>): <subject>

[optional body]
```

### Type 종류

| Type | 의미 | 사용 예시 |
|:---:|:---|:---|
| `feat` | ✅ 새로운 문제 해결 완료 | `feat(level2): solve '기능개발' using queue` |
| `attempt` | ❌ 문제 시도했으나 미해결 | `attempt(level2): failed '프린터' - need deque concept` |
| `refactor` | 🔄 기존 코드 개선/최적화 | `refactor(level1): optimize '두 개 뽑아서 더하기' to O(N)` |
| `fix` | 🐛 기존 코드의 버그 수정 | `fix(level2): resolve IndexError in '주식가격'` |
| `docs` | 📝 문서 작성/수정 | `docs(algorithm): add DFS/BFS concept explanation` |
| `test` | ✅ 테스트 케이스 추가 | `test(pccp): add edge cases for mock exam #1` |
| `chore` | 🔧 기타 (README 업데이트 등) | `chore: update weekly progress table` |

### Scope 종류
- `level1`, `level2`, `level3`: 프로그래머스 난이도
- `baekjoon`: 백준 문제
- `pccp`: PCCP 모의고사
- `algorithm`: 알고리즘 개념 정리
- `syntax`: Python-Java 문법 매핑

### Subject 작성 규칙
1. **50자 이내**로 간결하게
2. **명령문** 사용 (solve, add, fix, refactor)
3. **마침표 없음**
4. **한글 또는 영어** (혼용 가능하나 일관성 유지)

### Body 작성 (선택, 중요한 경우)
```
feat(level2): solve '타겟 넘버' using DFS

- Algorithm: Depth-First Search (Recursion)
- Time Complexity: O(2^N) - acceptable for N≤20
- Key Idea: 각 숫자를 +/- 선택하는 완전탐색
- Performance: 100% pass all test cases
- Solved in: 25분
```

---

## 📚 학습 리소스

### 핵심 플랫폼
- [프로그래머스 코딩테스트 고득점 Kit](https://school.programmers.co.kr/learn/challenges?tab=algorithm_practice_kit)
- [백준 온라인 저지](https://www.acmicpc.net/)
- [PCCP 자격증 안내](https://certi.programmers.co.kr/)

### 참고 자료
- **Python 알고리즘 인터뷰** (박상길 저)
- **이것이 취업을 위한 코딩 테스트다** (나동빈 저)
- **Java로 코딩테스트 합격하기** (김종관 저)

---

## 🔗 관련 링크

- **Notion 학습 데이터베이스**: [링크 추가 예정]
- **PCCP 응시 기록**: [링크 추가 예정]
- **개인 블로그/회고**: [링크 추가 예정]

---

## 💪 다짐 (Commitment)

> "하루도 빠짐없이, 한 문제씩 풀며 성장합니다.  
> 실패는 기록하고, 성공은 반복합니다.  
> 105일 후, PCCP Level 2 Java 자격증과 함께  
> 부트캠프 합격증을 들고 있을 나를 상상합니다."

**시작일**: 2026년 1월 4일 (토)  
**목표 완료일**: 2026년 4월 19일 (토)

---

## 📞 Contact

- **GitHub**: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)
- **Email**: your.email@example.com
- **Tech Blog**: [링크]

---

<div align="center">

**⭐ 이 리포지토리가 도움이 되셨다면 Star를 눌러주세요! ⭐**

![Footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer)

</div>