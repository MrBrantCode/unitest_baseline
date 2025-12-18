"""
QUESTION:
Given a binary matrix `grid` of dimensions `n x n`, write a function `shortestPathBinaryMatrix` to compute the length of the shortest unobstructed path from the top-left cell to the bottom-right cell, where an unobstructed path consists of 0s and 8-directionally connected cells. If no such path exists, return `-1`. The function must only consider cells with a value of 0, avoiding obstacles marked as 1. The constraints are: `n == grid.length`, `n == grid[i].length`, `1 <= n <= 100`, and `grid[i][j] is 0 or 1`.
"""

from queue import Queue

def shortestPathBinaryMatrix(grid):
    n = len(grid)
    if grid[0][0] or grid[n-1][n-1]:
        return -1
    q = Queue()
    q.put((0, 0, 1))
    grid[0][0] = 1 
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    while not q.empty():
        i, j, d = q.get()
        if i == j == n - 1:
            return d
        for x, y in directions:
            ni, nj = i + x, j + y
            if 0 <= ni < n and 0 <= nj < n and not grid[ni][nj]:
                q.put((ni, nj, d + 1))
                grid[ni][nj] = 1
    return -1