"""
QUESTION:
Implement a function named `rotate_matrix` that takes a 2D matrix of any size as input and modifies it in-place to rotate the matrix 90 degrees clockwise. The function should return the modified matrix.
"""

def rotate_matrix(matrix):
    n = len(matrix)  # Number of rows in the matrix

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row of the transposed matrix
    for i in range(n):
        matrix[i] = matrix[i][::-1]

    return matrix