"""
QUESTION:
You are tasked with implementing a function `largestContinent` that determines the size of the largest continent in a given world map represented by a 2D grid. The grid consists of integers where each cell represents a piece of land and the value in each cell indicates the continent to which it belongs. A continent is a connected region of land cells with the same value. The function should take a 2D grid of integers as input and return the size of the largest continent in the grid. The function should only traverse each cell in the grid once and should handle grids of any size.
"""

from collections import deque

def largestContinent(grid):
    def is_valid(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])

    def bfs(x, y, continent):
        queue = deque([(x, y)])
        size = 0
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        while queue:
            cx, cy = queue.popleft()
            if visited[cx][cy]:
                continue
            visited[cx][cy] = True
            size += 1
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = cx + dx, cy + dy
                if is_valid(nx, ny) and grid[nx][ny] == continent and not visited[nx][ny]:
                    queue.append((nx, ny))
        return size

    max_continent_size = 0
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if not visited[i][j] and grid[i][j] != 0:
                size = bfs(i, j, grid[i][j])
                max_continent_size = max(max_continent_size, size)
    return max_continent_size