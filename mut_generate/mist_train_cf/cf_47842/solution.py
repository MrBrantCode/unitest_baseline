"""
QUESTION:
Write a function `numPaths(m, n)` that calculates the total count of distinct routes leading from the bottom left corner to the top right corner of an m x n grid, where movement is restricted to upward or rightward transitions.
"""

def numPaths(m, n):
    dp = [[0 for x in range(n+1)] for x in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 1 or j == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m][n]