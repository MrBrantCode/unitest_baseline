"""
QUESTION:
Given a `m * n` matrix of ones and zeros, write a function named `countSquares` that returns two values: the number of square submatrices with all ones and the number of square submatrices with all zeros. The constraints are `1 <= m <= 300` and `1 <= n <= 300`.
"""

def countSquares(matrix):
    if not matrix: return 0, 0
    m, n = len(matrix), len(matrix[0])
    dpone, dpzero = [[0]*n for _ in range(m)], [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                dpone[i][j] = 1 if i == 0 or j == 0 else min(dpone[i-1][j], dpone[i][j-1], dpone[i-1][j-1]) + 1
            else:
                dpzero[i][j] = 1 if i == 0 or j == 0 else min(dpzero[i-1][j], dpzero[i][j-1], dpzero[i-1][j-1]) + 1
                
    return sum(sum(row) for row in dpone), sum(sum(row) for row in dpzero)