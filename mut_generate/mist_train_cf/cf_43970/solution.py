"""
QUESTION:
You are given a 2D binary matrix `isWater` of size `m x n`, where `0` represents land and `1` represents water. Your task is to assign a non-negative height to each cell such that the absolute difference in height between any two adjacent cells does not exceed `1`, the height of water cells is `0`, and the height of land cells is the minimum distance to the nearest water cell. Return an `m x n` matrix `height` where `height[i][j]` represents the height of cell `(i, j)`. If multiple solutions exist, return the one that maximizes the highest point in the matrix.

Constraints: `m == isWater.length`, `n == isWater[i].length`, `1 <= m, n <= 1000`, `isWater[i][j]` is `0` or `1`, and at least one water cell is guaranteed to be present. Implement the function `highestPeak(isWater)`.
"""

from collections import deque

def highestPeak(isWater):
    m, n = len(isWater), len(isWater[0])
    heights = [[0]*n for _ in range(m)]
    queue = deque()
    
    for i in range(m):
        for j in range(n):
            if isWater[i][j] == 1:
                heights[i][j] = 0
                queue.append((i,j))
                
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] == 0 and isWater[nx][ny] == 0:
                heights[nx][ny] = heights[x][y] + 1
                queue.append((nx, ny))
                
    return heights