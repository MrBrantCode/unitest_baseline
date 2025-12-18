"""
QUESTION:
Write a function named `rotate_matrix` that takes a square matrix as input and modifies it in-place by rotating it 90 degrees clockwise. The matrix is represented as a two-dimensional list where each inner list represents a row. The function should return the modified matrix.
"""

def rotate(matrix):
    n = len(matrix)
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]
            matrix[first][i] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[i][last]
            matrix[i][last] = top
    return matrix