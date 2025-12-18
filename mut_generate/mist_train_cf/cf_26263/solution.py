"""
QUESTION:
Implement a function called `rotate_2d_matrix` that takes a 2D square matrix as input and returns the matrix rotated 90 degrees clockwise. The input matrix is a list of lists where each inner list has the same length and represents a row in the matrix. The function should only work with square matrices (i.e., the number of rows is equal to the number of columns).
"""

def rotate_2d_matrix(matrix):
    n = len(matrix[0])
    m = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            m[i][j] = matrix[n-j-1][i]
    return m