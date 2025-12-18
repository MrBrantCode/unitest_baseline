"""
QUESTION:
Write a function `getFood(grid)` that takes a character matrix `grid` as input, where `grid` is a 2D array of characters of dimensions `m x n`, `m == grid.length`, `n == grid[i].length`, and `1 <= m, n <= 200`. The function should return the length of the shortest path from the cell containing `'*'` to any cell containing `'#'` in the grid. If no such path exists, return `-1`. The grid cells are `'*'` (your current position), `'#'` (food), `'O'` (free space), and `'X'` (obstacle). Movement is allowed to adjacent cells (north, east, south, or west) if there is no obstacle.
"""

from collections import deque

def getFood(grid):
    m, n = len(grid), len(grid[0])
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '*':
                start = (i, j)
    queue = deque([(*start, 0)])
    visited = {start}
    while queue:
        x, y, step = queue.popleft()
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != 'X' and (nx, ny) not in visited:
                if grid[nx][ny] == '#':
                    return step + 1
                queue.append((nx, ny, step + 1))
                visited.add((nx, ny)) 
    return -1