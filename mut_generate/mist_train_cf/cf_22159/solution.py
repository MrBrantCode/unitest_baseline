"""
QUESTION:
Write a function called `transpose_matrix` that takes a matrix A of dimensions m x n as input, where m and n are positive integers, and returns its transpose by swapping rows with columns. The function should have a time complexity of O(m x n) or better.
"""

def transpose_matrix(A):
    m = len(A)
    n = len(A[0])

    # Create a new matrix with dimensions n x m for the transpose
    result = [[0] * m for _ in range(n)]

    # Iterate through each element of A and swap its row and column indices
    for i in range(m):
        for j in range(n):
            result[j][i] = A[i][j]

    return result