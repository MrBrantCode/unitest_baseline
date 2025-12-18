"""
QUESTION:
Implement a function named `subtract_matrices` that takes two matrices A and B of size n x m, where n is the number of rows and m is the number of columns, and returns a new matrix C of the same size containing the result of subtracting matrix B from matrix A. The elements of A and B are integers.
"""

def subtract_matrices(A, B):
    n = len(A)  
    m = len(A[0])  

    C = [[0 for j in range(m)] for i in range(n)]

    for i in range(n):
        for j in range(m):
            C[i][j] = A[i][j] - B[i][j]

    return C