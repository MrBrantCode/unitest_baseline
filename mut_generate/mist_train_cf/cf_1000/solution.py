"""
QUESTION:
Write a function named `rotate_matrix` to rotate a square matrix by 90 degrees in a clockwise direction. The input matrix is a two-dimensional list of integers, with a maximum size of 100x100 and elements in the range [0, 1000]. The function should modify the matrix in-place.
"""

def rotate_matrix(matrix):
    n = len(matrix)  # number of rows/columns in the matrix
    
    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]
    
    return matrix