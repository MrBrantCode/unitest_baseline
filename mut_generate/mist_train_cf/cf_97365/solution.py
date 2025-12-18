"""
QUESTION:
Implement a function `rotate_matrix(matrix)` that takes a 2D square matrix of integers as input, and rotates it 90 degrees clockwise in-place. The matrix can have any number of rows and columns, but it will always be a square matrix. The function should modify the original matrix instead of creating a new one, and the matrix elements will always be unique and within the range of -1000 to 1000.
"""

def rotate_matrix(matrix):
    n = len(matrix)  # Size of the matrix
    
    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row of the transposed matrix
    for i in range(n):
        matrix[i] = matrix[i][::-1]
    
    return matrix