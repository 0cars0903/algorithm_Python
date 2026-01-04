# 📋 Commit Convention Guide

## 🎯 왜 커밋 컨벤션이 중요한가?

부트캠프나 기업 채용 과정에서 GitHub 히스토리는 **가장 강력한 포트폴리오**입니다.  
체계적인 커밋 메시지는:
- ✅ **당신의 성장 과정**을 명확하게 보여줍니다
- ✅ **코드 리뷰 능력**을 증명합니다
- ✅ **프로페셔널한 협업 능력**을 어필합니다
- ✅ **자기주도 학습 능력**을 시각화합니다

---

## 📐 기본 구조

```
<type>(<scope>): <subject>

[optional body]

[optional footer]
```

### 예시
```
feat(level2): solve '프린터' using queue and priority

- Algorithm: Queue + Priority Queue simulation
- Time Complexity: O(N log N)
- Key Idea: 우선순위가 가장 높은 문서를 먼저 인쇄하는 시뮬레이션
- Difficulty: ★★★☆☆
- Solved in: 32분

Closes #15
```

---

## 🏷️ Type (반드시 지켜야 할 규칙)

### 핵심 Type

| Type | 언제 사용? | 커밋 예시 |
|:---:|:---|:---|
| `feat` | ✅ **문제를 성공적으로 해결했을 때** | `feat(level1): solve '두 개 뽑아서 더하기'` |
| `attempt` | ❌ **문제를 풀었으나 실패했을 때** | `attempt(level2): failed '튜플' - timeout on test 8` |
| `refactor` | 🔄 **기존 코드를 개선했을 때** | `refactor(level1): optimize '완주하지 못한 선수' to O(N)` |
| `fix` | 🐛 **이미 커밋한 코드의 버그를 수정했을 때** | `fix(level2): resolve IndexError in '다리를 지나는 트럭'` |
| `docs` | 📝 **문서(README, 개념 정리 등)를 작성/수정했을 때** | `docs(algorithm): add explanation for BFS algorithm` |
| `test` | ✅ **테스트 케이스를 추가했을 때** | `test(pccp): add edge case for mock exam problem #3` |
| `chore` | 🔧 **기타(README 통계 업데이트, 폴더 정리 등)** | `chore: update weekly progress in README.md` |

---

## 🎯 Scope (어떤 범위의 수정인지)

### 난이도별 Scope
- `level1`, `level2`, `level3`, `level4`, `level5`: 프로그래머스 난이도
- `baekjoon`: 백준 문제
- `pccp`: PCCP 모의고사

### 주제별 Scope
- `algorithm`: 알고리즘 개념 정리
- `syntax`: Python-Java 문법 비교
- `data-structure`: 자료구조 이론

---

## 📝 Subject (제목 작성 규칙)

### ✅ DO (이렇게 하세요)
```bash
✅ feat(level1): solve '완주하지 못한 선수' using hash
✅ attempt(level2): failed '소수 찾기' - permutation timeout
✅ refactor(level1): improve time complexity from O(N^2) to O(N)
✅ docs(algorithm): add DFS concept with examples
```

### ❌ DON'T (이렇게 하지 마세요)
```bash
❌ "update"
❌ "문제 풀었음"
❌ "fix bug"
❌ "level1 문제 3개 추가"
```

### 규칙 요약
1. **50자 이내**로 작성
2. **명령문** 사용 (solve, add, fix, refactor, update)
3. **마침표 없음**
4. **구체적으로** (문제 이름 포함)

---

## 📄 Body (본문 작성 - 선택 사항, 중요한 경우만)

### 언제 Body를 작성하나?
- ✅ 복잡한 알고리즘을 사용한 경우
- ✅ 성능 개선을 달성한 경우
- ✅ 특별한 인사이트가 있는 경우
- ✅ 실패한 이유를 상세히 기록하고 싶은 경우

### Body 작성 템플릿

#### 1. 문제 해결 (feat) 시
```
feat(level2): solve '타겟 넘버' using DFS

- Algorithm: Depth-First Search (Recursion)
- Time Complexity: O(2^N) - acceptable for N≤20
- Space Complexity: O(N) - recursion depth
- Key Idea: 각 숫자를 +/- 선택하는 완전탐색
- Difficulty: ★★★☆☆
- Solved in: 25분
- Reference: 프로그래머스 고득점 Kit - DFS/BFS
```

#### 2. 실패 (attempt) 시
```
attempt(level2): failed '가장 큰 수' - wrong answer on test 3

- Attempted Approach: 단순 내림차순 정렬
- Blocker: [3, 30, 34, 5, 9]의 경우 "9534330"이 정답이나 "9534303" 출력
- Root Cause: 문자열 비교 없이 숫자 크기만 비교
- Lesson Learned: 정렬 기준을 lambda로 커스터마이징해야 함
- Next Action: Python의 key 파라미터 학습 후 재도전
- Time Spent: 45분
```

#### 3. 리팩토링 (refactor) 시
```
refactor(level1): optimize '완주하지 못한 선수' from O(N^2) to O(N)

- Before: 이중 for문으로 완주자 리스트를 순회하며 제거
- After: collections.Counter()로 빈도수 차이 계산
- Performance Gain: 
  * 테스트 케이스 5: 1200ms → 80ms (15배 개선)
  * 메모리 사용량: 거의 동일
- Insight: Hash 자료구조의 O(1) 조회 성능 체감
```

---

## 🚀 실전 예시 모음

### 시나리오 1: Level 1 문제 성공
```bash
git add src/programmers/level1/solved/p42576_완주하지_못한_선수.py

git commit -m "feat(level1): solve '완주하지 못한 선수' using hash map

- Algorithm: Hash (Counter)
- Time Complexity: O(N)
- Key Idea: collections.Counter()로 빈도 차이 계산
- Solved in: 12분"
```

### 시나리오 2: Level 2 문제 실패
```bash
git add src/programmers/level2/failed/p42746_가장_큰_수_attempt.py

git commit -m "attempt(level2): failed '가장 큰 수' - wrong answer

- Attempted: 단순 내림차순 정렬
- Issue: [3, 30, 34]에서 "34330" 대신 "34303" 출력
- Blocker: 문자열 결합 시 최댓값 판단 로직 필요
- Next: lambda 커스텀 정렬 학습"
```

### 시나리오 3: 실패 후 재도전 성공
```bash
git add src/programmers/level2/solved/p42746_가장_큰_수.py

git commit -m "feat(level2): solve '가장 큰 수' after learning custom sort

- Algorithm: Custom Sorting with lambda
- Key Insight: 두 수를 문자열로 합쳤을 때 더 큰 것을 우선
- Lambda: key=lambda x: x*3 트릭 활용
- Improved from: failed attempt (see failed/ directory)
- Solved in: 18분"
```

### 시나리오 4: 알고리즘 개념 정리
```bash
git add docs/algorithms/dfs-bfs.md

git commit -m "docs(algorithm): add comprehensive DFS/BFS guide

- Topics: 
  * DFS 개념 및 재귀 구현
  * BFS 개념 및 큐 구현
  * 두 알고리즘의 차이점과 사용 시점
  * Python collections.deque 활용법
- Examples: 5개 문제 풀이 포함"
```

### 시나리오 5: PCCP 모의고사
```bash
git add src/pccp/mock-exam-1/

git commit -m "test(pccp): complete mock exam #1 with 720 points

Results:
- Problem 1: ✅ 250/250 (12분)
- Problem 2: ✅ 250/250 (18분)  
- Problem 3: ⚠️ 120/250 (35분) - partial score
- Problem 4: ⚠️ 100/250 (45분) - timeout on large inputs

Analysis:
- Strong: Stack/Queue, Hash 완벽 처리
- Weak: DP 문제에서 시간 복잡도 실패
- Action: DP 유형 집중 학습 필요"
```

### 시나리오 6: 주간 통계 업데이트
```bash
git add README.md

git commit -m "chore: update Week 2 progress statistics

- Level 1: 40 solved (100%)
- Level 2: 15 solved (target: 10)
- Study streak: 14 days 🔥
- Total problems: 55 (+15 from last week)"
```

---

## 💡 Pro Tips

### 1. 커밋은 자주, 작게
❌ 나쁜 예: 일주일 치 문제 10개를 한 번에 커밋
```bash
git add .
git commit -m "update"  # 😱 최악!
```

✅ 좋은 예: 문제 하나 풀 때마다 즉시 커밋
```bash
# 문제 1 해결
git add src/programmers/level1/solved/p42576_완주하지_못한_선수.py
git commit -m "feat(level1): solve '완주하지 못한 선수' using hash"

# 문제 2 해결
git add src/programmers/level1/solved/p42748_K번째수.py  
git commit -m "feat(level1): solve 'K번째수' using sort and slice"
```

### 2. 실패도 당당하게 기록하라
실패는 **성장의 증거**입니다. `attempt` 타입으로 실패를 기록하면:
- 어떤 접근을 시도했는지 명확히 남음
- 같은 실수를 반복하지 않음
- 성장 과정을 투명하게 보여줌

### 3. Emoji 활용 (선택 사항)
더 시각적으로 만들고 싶다면:
```bash
git commit -m "✨ feat(level2): solve '프린터' using queue"
git commit -m "❌ attempt(level3): failed '이중우선순위큐'"
git commit -m "📝 docs(algorithm): add heap explanation"
git commit -m "🐛 fix(level1): resolve edge case in '신규 아이디 추천'"
```

### 4. Issue 번호와 연결
GitHub Issues를 사용한다면:
```bash
git commit -m "feat(level2): solve '소수 찾기'

Closes #23"
```

---

## 🔗 참고 자료

- [Conventional Commits 공식 문서](https://www.conventionalcommits.org/)
- [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)
- [AngularJS Commit Convention](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#commit)

---

## ⚡ Quick Reference

```bash
# 문제 해결 성공
feat(level1): solve '문제명' using 알고리즘명

# 문제 실패
attempt(level2): failed '문제명' - 실패 이유

# 재도전 성공
feat(level2): solve '문제명' after learning 새로운개념

# 코드 개선
refactor(level1): optimize '문제명' from O(N^2) to O(N)

# 버그 수정
fix(level2): resolve IndexError in '문제명'

# 문서 작성
docs(algorithm): add 알고리즘명 explanation

# 주간 업데이트
chore: update weekly progress statistics
```
