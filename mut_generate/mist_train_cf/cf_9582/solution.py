"""
QUESTION:
Rotate a given square matrix by 90 degrees in a clockwise direction. The input matrix will be a list of lists where each inner list represents a row in the matrix and contains the same number of elements as the number of inner lists. The function should return the rotated matrix.

The function name should be `rotate_matrix(matrix)`.
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