from collections import deque

def solution(land):
    n, m = len(land), len(land[0])
    visited = [[False] * m for _ in range(n)]
    oil_groups = {}
    group_id = 2
    
    def bfs(si, sj):
        q = deque([(si, sj)])
        visited[si][sj] = True
        land[si][sj] = group_id
        size = 1
        
        while q:
            i, j = q.popleft()
            for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                ni, nj = i+di, j+dj
                if 0<=ni<n and 0<=nj<m and not visited[ni][nj] and land[ni][nj]==1:
                    visited[ni][nj] = True
                    land[ni][nj] = group_id
                    q.append((ni, nj))
                    size += 1
        return size
    
    # 1. 모든 덩어리 찾기 & 라벨링
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                oil_groups[group_id] = bfs(i, j)
                group_id += 1
    
    # 2. 각 열마다 최대 석유량 계산
    max_oil = 0
    for col in range(m):
        groups = set(land[row][col] for row in range(n) if land[row][col] >= 2)
        max_oil = max(max_oil, sum(oil_groups[gid] for gid in groups))
    
    return max_oil