"""
QUESTION:
Write a function named `maxProductPath` that takes a 2D matrix `grid` as input, with values representing hexadecimal digits. Return the maximum product of any path from the top-left to the bottom-right of the grid, where the path can move right or down at any point, and the product is calculated using hexadecimal multiplication. The function must handle potential overflow errors and multiplication by zero.
"""

def maxProductPath(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = int(grid[0][0], 16)
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] * int(grid[i][0], 16)
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] * int(grid[0][j], 16)
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) * int(grid[i][j], 16)
            if dp[i][j] < -(2**31):
                return -1
    return dp[-1][-1]