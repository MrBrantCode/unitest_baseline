"""
QUESTION:
Write a function `shortestDistance(grid)` that takes a 2D grid as input, where `0` represents an empty land, `1` represents a building, and `2` represents an obstacle. The function should return the minimum total travel distance to all buildings from an empty land, calculated using the Manhattan Distance formula. If no such empty land exists, return `-1`. The grid's dimensions `m` and `n` satisfy `1 <= m, n <= 100` and `grid[i][j]` can only be `0`, `1`, or `2`.
"""

from collections import deque

def shortestDistance(grid):
    if not grid or not grid[0]: 
        return -1

    m, n = len(grid), len(grid[0])
    dist = [[0]*n for _ in range(m)]
    reach = [[0]*n for _ in range(m)]
    buildings = sum(val == 1 for line in grid for val in line)

    def BFS(start_x, start_y):
        direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = [[False]*n for _ in range(m)]
        visited[start_x][start_y], count1, queue = True, 1, deque([(start_x, start_y, 0)])
        while queue:
            x, y, d = queue.popleft()
            for dx, dy in direct:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 0:
                    queue.append((nx, ny, d + 1))
                    visited[nx][ny] = True
                    dist[nx][ny] += d + 1
                    reach[nx][ny] += 1

    for x in range(m):
        for y in range(n):
            if grid[x][y] == 1:
                BFS(x, y)

    return min([dist[i][j] for i in range(m) for j in range(n) if not grid[i][j] and reach[i][j] == buildings] or [-1])