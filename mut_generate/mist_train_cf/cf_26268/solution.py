"""
QUESTION:
Given a 2D matrix of integers, write a function `max_sum_submatrix(matrix)` that returns the maximum sum of a submatrix within the given matrix. The function should only take the matrix as input and return the maximum sum. The matrix is guaranteed to be a list of lists where each inner list has the same length, representing the rows and columns of the matrix.
"""

def max_sum_submatrix(matrix):
    rows, columns = len(matrix), len(matrix[0])
    dp = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            dp[i][j] = matrix[i][j]
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]
            if i > 0 and j > 0:
                dp[i][j] -= dp[i-1][j-1]
                
    max_sum = float('-inf')
    for r1 in range(rows):
        for r2 in range(r1, rows):
            for c1 in range(columns):
                for c2 in range(c1, columns):
                    current_sum = dp[r2][c2]
                    if r1 > 0:
                        current_sum -= dp[r1-1][c2]
                    
                    if c1 > 0:
                        current_sum -= dp[r2][c1-1]
                    
                    if r1 > 0 and c1 > 0:
                        current_sum += dp[r1-1][c1-1]
                    
                    max_sum = max(max_sum, current_sum)
    return max_sum