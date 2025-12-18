"""
QUESTION:
Write a function named `transpose_matrix` that takes a 2D list `A` as input and returns its transpose. The transpose of a matrix is obtained by swapping its rows with its columns. The function should work for any given matrix with dimensions m x n, where m and n are positive integers.
"""

def transpose_matrix(A):
    m = len(A)       # number of rows of A
    n = len(A[0])    # number of columns of A
    
    # create a new matrix B with dimensions n x m
    B = [[0 for _ in range(m)] for _ in range(n)]
    
    # assign elements from A to B
    for i in range(m):
        for j in range(n):
            B[j][i] = A[i][j]
    
    return B