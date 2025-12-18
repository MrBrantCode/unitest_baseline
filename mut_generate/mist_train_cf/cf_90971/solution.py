"""
QUESTION:
Write a function `rotate_matrix(matrix)` that takes a square matrix as input and returns the rotated matrix by 90 degrees in a clockwise direction. The input matrix is a list of lists where each inner list has the same length, representing the rows of the matrix. The function should modify the input matrix in-place and return the rotated matrix.
"""

def rotate_matrix(matrix):
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]
    return matrix