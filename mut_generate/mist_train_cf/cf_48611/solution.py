"""
QUESTION:
Write a function `min_squares(n, m)` that takes two integers `n` and `m` as input, representing the dimensions of a rectangle, and returns the minimum number of squares with integer sides required to completely tile the given rectangle. The function should work for `1 <= n, m <= 13`.
"""

def min_squares(n, m):
    dp = [[0]*(m+1) for _ in range(n+1)] 
      
    for i in range(1, n+1):
        for j in range(1, m+1):
            if (i==j):
                dp[i][j] = 1
            else:
                min_sq = float('inf')
                for k in range(1, i // 2 + 1):
                    min_sq = min(min_sq, dp[k][j] + dp[i-k][j])
                for k in range(1, j // 2 + 1):
                    min_sq = min(min_sq, dp[i][k] + dp[i][j-k])
                dp[i][j] = min_sq
    return dp[n][m]