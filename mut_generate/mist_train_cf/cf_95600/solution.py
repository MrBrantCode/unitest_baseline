"""
QUESTION:
Write a Python function `transpose_matrix(matrix)` that takes a 2D array as input, checks if it's a square matrix, and returns its transpose. If the input is not a square matrix, the function should raise an exception. The input matrix contains integers ranging from -10^9 to 10^9.
"""

def transpose_matrix(matrix):
    # Check if the input matrix is a square matrix
    if len(matrix) != len(matrix[0]):
        raise Exception("Input matrix is not a square matrix")

    # Transpose the matrix
    transposed = []
    for i in range(len(matrix[0])):
        transposed.append([row[i] for row in matrix])

    return transposed