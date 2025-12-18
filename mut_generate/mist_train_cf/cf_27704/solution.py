"""
QUESTION:
You are given a grid with m rows and n columns, where 1 <= m, n <= 100. Write a function `uniquePaths` to calculate the total number of unique paths from the top-left corner to the bottom-right corner, where you can only move either down or right in each step. The function should take two integers m and n as input and return the total number of unique paths.
"""

def uniquePaths(m: int, n: int) -> int:
    dp = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]