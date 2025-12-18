"""
QUESTION:
Write a function `minPathWithBlockedCells(grid, k, blockedCells)` that returns an ordered list representing the numeric values on the shortest path in an N x N grid, avoiding certain blocked cells. The function should start from any cell and move edge-to-edge to any adjacent cell, ensuring the path does not exceed the grid boundaries. The path length is `k` cells. The `grid` is a 2D list of integers, `k` is an integer, and `blockedCells` is a list of tuples representing the blocked cell coordinates.
"""

from typing import List, Tuple

def minPathWithBlockedCells(grid: List[List[int]], k: int, blockedCells: List[Tuple[int, int]]) -> List[int]:
    n = len(grid)
    blocked = [[False]*n for _ in range(n)]
    for x, y in blockedCells:
        blocked[x][y] = True

    dp = [[float('inf')]*n for _ in range(n)]  # Initialize with largest possible value
    path = [['']*n for _ in range(n)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, left, down, up

    def dfs(x: int, y: int, k: int) -> int:
        if k == 0:
            path[x][y] = str(grid[x][y])
            return grid[x][y]
        if dp[x][y] != float('inf'):
            return dp[x][y]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not blocked[nx][ny]:
                val = dfs(nx, ny, k - 1) + grid[x][y]
                if val < dp[x][y]:
                    dp[x][y] = val
                    path[x][y] = str(grid[x][y]) + ' ' + path[nx][ny]
        return dp[x][y]

    minVal = float('inf')
    minPath = ''
    for i in range(n):
        for j in range(n):
            if not blocked[i][j]:
                dfs(i, j, k - 1)
                if dp[i][j] < minVal:
                    minVal = dp[i][j]
                    minPath = path[i][j]
    return list(map(int, minPath.split()))