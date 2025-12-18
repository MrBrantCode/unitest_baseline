"""
QUESTION:
Write a function named `rotate` that takes a 2D list (matrix) as input, rotates it 90 degrees clockwise in-place, and returns the rotated matrix. The function should be efficient for large matrices.
"""

def rotate(matrix):
    n = len(matrix)
    # transpose matrix
    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i] 

    # reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]

    return matrix