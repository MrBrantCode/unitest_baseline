"""
QUESTION:
Write a function named `transpose` that takes a non-square 2D matrix as input and returns its transpose. The function should create a new matrix that is the transpose of the input matrix. Note that it is not possible to perform this operation in-place without using additional space, so the function should use extra space to store the transposed matrix.
"""

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]