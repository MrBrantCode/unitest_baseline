"""
QUESTION:
Create a function named `transpose_matrix` that takes a 2D array as an argument. The function should return a new 2D array that is the transposed version of the input array, but only if the input array is a square matrix (i.e., it has the same number of rows and columns). If the input array is not a square matrix, the function should raise an exception.
"""

def transpose_matrix(matrix):
    # Check if the input matrix is a square matrix
    if len(matrix) != len(matrix[0]):
        raise Exception("Input matrix is not a square matrix")

    # Transpose the matrix
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]