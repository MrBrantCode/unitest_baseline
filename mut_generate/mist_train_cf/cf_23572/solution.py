"""
QUESTION:
Write a function called `rotate_matrix` that takes a square matrix as input and returns the matrix rotated by 90 degrees clockwise. The function should assume the input matrix is a list of lists where each inner list has the same length, representing the rows of the matrix. The function should return a new rotated matrix without modifying the original input.
"""

def rotate_matrix(matrix):
    m = len(matrix)
    # Create a new matrix
    new_matrix = [[0 for _ in range(m)] for _ in range(m)]
    # Rotate the matrix
    for i in range(m):
        for j in range(m): 
            new_matrix[j][m - i - 1] = matrix[i][j]
    # Return the rotated matrix
    return new_matrix