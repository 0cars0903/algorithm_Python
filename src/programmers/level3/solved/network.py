from collections import deque

def solution(n, computers):
    answer = 0
    
    visited = [False] * n
    
    Q = deque()
    points = [0]
    
    while points:
        Q.append(points[0])
        while Q:
            p0 = Q.popleft()
            visited[p0] = True
            for i in range(n):
                if visited[i] == False:
                    if computers[p0][i] == 1:
                        visited[i] = True
                        Q.append(i)

        answer += 1
        
        points = []
        for i in range(n):
            if visited[i] == False:
                points.append(i)
        
    return answer 