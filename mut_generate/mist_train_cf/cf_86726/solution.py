"""
QUESTION:
Write a function called `rotate_matrix` that takes a square matrix as input, represented as a two-dimensional list, and modifies it in-place by rotating it 90 degrees in a clockwise direction. The size of the matrix will be at most 100x100, and the matrix elements will be integers in the range [0, 1000].
"""

def rotate_matrix(matrix):
    n = len(matrix)  
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i] = matrix[i][::-1]
    return matrix