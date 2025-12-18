"""
QUESTION:
Implement the function maximumPath(grid, k) that performs a depth-first search on a grid with memoization. The function should return the maximum sum that can be obtained by moving right, down, left, or up from any cell in the grid for at most k steps. If the grid is empty or has no valid paths, return None. The function should handle a grid of any size and k value.
"""

import sys

def maximumPath(grid, k):
    if not grid or len(grid) == 0 or len(grid[0]) == 0:
        return None

    rows, cols = len(grid), len(grid[0])
    memo = [[[-sys.maxsize] * (k + 1) for _ in range(cols)] for _ in range(rows)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

    def dfs(x, y, k):
        if x < 0 or y < 0 or k < 0 or x >= rows or y >= cols or memo[x][y][k] != -sys.maxsize:
            return -sys.maxsize

        if k == 1:
            return grid[x][y]

        res = -sys.maxsize
        for dx, dy in directions:
            res = max(res, grid[x][y] + dfs(x + dx, y + dy, k - 1))

        memo[x][y][k] = res
        return res

    return max(dfs(i, j, k) for i in range(rows) for j in range(cols) if dfs(i, j, k) != -sys.maxsize)