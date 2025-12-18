"""
QUESTION:
Formulate a function `formulate_matrix(N, M)` that creates a matrix of size N x M where each row sum equals the product of its indexes (N*M for all N,M in the matrix) and each column sum is even, using non-negative integers.
"""

def formulate_matrix(N, M):
    matrix = [[0 for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            matrix[i][j] = (i+1)*(j+1)
    
    for j in range(M):
        column_sum = sum(matrix[i][j] for i in range(N))
        if column_sum % 2 != 0 and N>0:  
            matrix[N-1][j] += 1

    return matrix