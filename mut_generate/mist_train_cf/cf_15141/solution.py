"""
QUESTION:
Write a function named `reverse_matrix` that takes a 2D list of numbers (matrix) as input and returns a new matrix where the order of rows and columns are reversed. The input matrix will have at least 2 rows and 2 columns, and it may not be a square matrix.
"""

def reverse_matrix(matrix):
    new_matrix = []
    for j in range(len(matrix[0])):  # iterate over columns
        new_row = []
        for i in range(len(matrix)):  # iterate over rows
            new_row.append(matrix[i][j])
        new_matrix.append(new_row)
    return new_matrix