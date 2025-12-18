"""
QUESTION:
Implement a function `uniquePaths` that calculates the total number of unique paths to reach the bottom-right corner of a grid from the top-left corner, where you can only move down or right, and cannot travel through obstacles (represented as 1 in the grid, with 0 representing empty space). The function should take a 2D grid as input and return the total number of unique paths.
"""

from typing import List

def uniquePaths(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:  # obstacle
                dp[i][j] = 0
            elif i == 0 and j == 0:  # start position
                dp[i][j] = 1
            elif i == 0:  # first row
                dp[i][j] = dp[i][j-1]
            elif j == 0:  # first column
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m-1][n-1]