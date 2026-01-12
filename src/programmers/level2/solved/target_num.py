from collections import deque

def solution(numbers, target):
    Q = deque()
    Q.append(0)
    answer = 0
    while len(Q) < len(numbers)**2:
        for i in range(len(numbers)):
            L = len(Q)
            for _ in range(L):
                n = Q.popleft()
                a = n + numbers[i]
                b = n - numbers[i]
                Q.append(a)
                Q.append(b)
    answer = Q.count(target)
    return answer