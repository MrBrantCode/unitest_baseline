"""
QUESTION:
Given a grid with m rows and n columns, implement the function `getFood(grid)` to find the length of the shortest path from the cell marked '*' to any cell marked '#'. The grid contains the following types of cells: '*' (starting point), '#' (food), 'O' (free space), 'X' (obstacle), and 'T' (trap that takes twice as long to traverse). If no path exists, return -1.
"""

from collections import deque

def getFood(grid):
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    m, n = len(grid), len(grid[0])
    dist = [[float('inf')]*n for _ in range(m)]
    q = deque([])

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '*': 
                dist[i][j] = 0
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and dist[nx][ny] == float('inf'):
                if grid[nx][ny] == 'X':
                    continue
                elif grid[nx][ny] == 'O' or grid[nx][ny] == '#':
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
                elif grid[nx][ny] == 'T':
                    dist[nx][ny] = dist[x][y] + 2
                    q.append((nx, ny))

    food_dist = min(dist[i][j] for i in range(m) for j in range(n) if grid[i][j] == '#')
    return food_dist if food_dist != float('inf') else -1