"""
QUESTION:
Write a function called `find_max_sum` that takes a 2D array `grid` of positive and negative integers as input, and returns the maximum sum of numbers that can be obtained by tracing a path from the top-left to bottom-right corner. The path can only move down or right at each step.
"""

def find_max_sum(grid):
    m = len(grid)
    n = len(grid[0])

    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]

    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    return dp[m-1][n-1]