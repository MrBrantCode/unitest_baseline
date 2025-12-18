"""
QUESTION:
Write a function `matrix_sum` that takes two matrices `A` and `B` as input, each of size m x n. The function should return a new matrix `C` of the same size, where `C[i][j] = A[i][j] + B[i][j]` for all i and j. Assume that the input matrices are valid (i.e., they have the same dimensions).
"""

def matrix_sum(A, B): 
    m = len(A) 
    n = len(A[0]) 
    C = [[0 for i in range(n)] for j in range(m)] 
    for i in range(m):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C