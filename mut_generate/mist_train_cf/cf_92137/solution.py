"""
QUESTION:
Write a function `uniquePaths(n: int, m: int) -> int` to calculate the total number of unique paths from the top-left corner to the bottom-right corner of an N x M matrix, where you can only move down or right in each step. The function should have a time complexity of O(N*M) or better.
"""

def uniquePaths(n: int, m: int) -> int:
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[n-1][m-1]