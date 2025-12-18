"""
QUESTION:
Write two functions, `rotate_matrix_clockwise(matrix)` and `rotate_matrix_counterclockwise(matrix)`, that take a square matrix of size n x n as input and return the rotated matrix by 90 degrees in the clockwise and counterclockwise directions respectively. The size of the matrix will be at most 100x100 and the elements in the matrix will be integers.
"""

def rotate_matrix_clockwise(matrix):
    n = len(matrix)
    rotated_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_matrix[j][n-1-i] = matrix[i][j]
    return rotated_matrix

def rotate_matrix_counterclockwise(matrix):
    n = len(matrix)
    rotated_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_matrix[n-1-j][i] = matrix[i][j]
    return rotated_matrix