"""
QUESTION:
Write a function named `add_matrices` that takes two n-dimensional matrices A and B as input, where each matrix can have up to 10^3 x 10^3 integer elements. The function should return the resulting matrix after the summation of A and B, given that A and B are the same size.
"""

def add_matrices(A, B):
    # A and B are lists (matrices with integers values).
    assert len(A) == len(B), "Matrices should have same size"
    assert len(A[0]) == len(B[0]), "Matrices should have same size"
    
    rows = len(A)
    cols = len(A[0])
    
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            result[i][j] = A[i][j] + B[i][j]
    
    return result