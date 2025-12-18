"""
QUESTION:
Given a 2D matrix of integers, write a function `max_sum_submatrix(matrix)` to retrieve the maximum sum submatrix. The function should return the maximum sum. The matrix can have a maximum size of 1000 x 1000, and the elements in the matrix can have a maximum value of 10000. If the matrix is empty, return 0 as the maximum sum. If multiple submatrices have the same maximum sum, return any one of them.
"""

def max_sum_submatrix(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = matrix[0][0]
    max_sum = float('-inf')
    
    # compute dp matrix
    for i in range(m):
        for j in range(n):
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]
            if i > 0 and j > 0:
                dp[i][j] -= dp[i-1][j-1]
            dp[i][j] += matrix[i][j]
            
    # find maximum sum submatrix
    for i in range(m):
        for j in range(n):
            for k in range(i, m):
                for l in range(j, n):
                    submatrix_sum = dp[k][l]
                    if i > 0:
                        submatrix_sum -= dp[i-1][l]
                    if j > 0:
                        submatrix_sum -= dp[k][j-1]
                    if i > 0 and j > 0:
                        submatrix_sum += dp[i-1][j-1]
                    max_sum = max(max_sum, submatrix_sum)
                    
    return max_sum