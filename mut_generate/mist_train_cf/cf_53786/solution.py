"""
QUESTION:
Given an `m x n` binary matrix filled with `0`'s, `1`'s and `2`'s, write a function `maximalSquare(matrix)` that finds the largest square containing only `1`'s and returns its area. The `2`'s in the matrix represent obstacles and cannot be part of the square. The matrix constraints are: `1 <= m, n <= 300` and `matrix[i][j]` is `'0'`, `'1'` or `'2'`.
"""

def maximalSquare(matrix):
    if not matrix or not matrix[0]: return 0

    m, n = len(matrix), len(matrix[0])
    dp = [[0]*n for _ in range(m)]
    max_edge = 0
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':
                if i==0 or j==0:   # edge case
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                max_edge = max(max_edge, dp[i][j])
                
    return max_edge * max_edge