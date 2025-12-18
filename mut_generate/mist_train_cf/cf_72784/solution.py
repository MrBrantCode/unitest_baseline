"""
QUESTION:
Create a function called `minCost(grid)` where `grid` is a 2D list of integers representing a grid of cells, each containing a sign pointing to the next cell. The signs can be 1 (right), 2 (left), 3 (down), 4 (up), or 0 (obstacle). Return the minimum cost to make the grid have at least one valid path from the top-left cell to the bottom-right cell, where a valid path is a path that follows the signs. You can modify the sign on a cell with a cost of 1, but you cannot modify the sign of an obstacle cell. If it's impossible to make a valid path, return -1. The grid has at most 100 rows and columns.
"""

from collections import deque

def minCost(grid):
    m, n = len(grid), len(grid[0])
    moves = [(0,1,1),(0,-1,2),(1,0,3),(-1,0,4)]
    cost = [[float('inf')]*n for _ in range(m)]
    cells = deque([(0,0,0)])
    
    while cells:
        x, y, c = cells.popleft()
        if x == m - 1 and y == n - 1: 
            return c
        for dx, dy, v in moves:
            nx, ny = x + dx, y + dy
            nc = c if 0 <= nx < m and 0 <= ny < n and grid[x][y] == v else c+1
            if 0 <= nx < m and 0 <= ny < n and cost[nx][ny] > nc:
                cost[nx][ny] = nc
                if (grid[x][y] == v):
                    cells.appendleft((nx, ny, nc))
                else:
                    cells.append((nx, ny, nc))

    return -1