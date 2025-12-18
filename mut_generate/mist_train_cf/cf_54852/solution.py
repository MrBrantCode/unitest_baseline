"""
QUESTION:
Write a function `minTotalDistance(grid)` that takes a binary grid `grid` as input where each `1` marks the home of one friend, and each `2` marks an obstacle. The function should return the minimal total travel distance, which is the sum of the distances between the houses of the friends and the meeting point. The distance is calculated using Manhattan Distance, where `distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|`. The friends cannot pass through obstacles. If there is no cell that can reach all friends' houses, return -1. The grid size is `m x n` where `1 &lt;= m, n &lt;= 200`.
"""

from collections import deque

def minTotalDistance(grid):
    m, n = len(grid), len(grid[0])
    directions = [(0,1), (1,0), (-1,0), (0,-1)]
    friends = [(i,j) for i in range(m) for j in range(n) if grid[i][j] == 1]
    obstacles = [(i,j) for i in range(m) for j in range(n) if grid[i][j] == 2]
    min_distance = float('inf')
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                dist = [[-1]*n for _ in range(m)] 
                dist[i][j] = 0
                queue = deque([(i,j)]) 
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0<=nx<m and 0<=ny<n and dist[nx][ny]==-1 and grid[nx][ny]!=2:
                            dist[nx][ny] = dist[x][y] + 1
                            queue.append((nx, ny))
                total_distance = sum(dist[x][y] for x,y in friends)
                min_distance = min(min_distance, total_distance)
    return min_distance if min_distance!=float('inf') else -1