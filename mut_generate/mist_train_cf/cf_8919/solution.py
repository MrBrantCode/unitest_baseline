"""
QUESTION:
Write a function `reverse_matrix` that takes a 2D list (matrix) with at least 2 rows and 2 columns as input, and returns a new matrix where the order of rows and columns is reversed. The function should work with matrices of any size, with the number of rows and columns being greater than or equal to 2.
"""

def reverse_matrix(matrix):
    # Get the number of rows and columns in the matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Create a new matrix with reversed rows and columns
    reversed_matrix = [[None] * num_rows for _ in range(num_cols)]
    for i in range(num_rows):
        for j in range(num_cols):
            reversed_matrix[j][i] = matrix[i][j]

    return reversed_matrix