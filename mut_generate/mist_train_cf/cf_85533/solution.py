"""
QUESTION:
Implement a function `print_columns(matrix, num_of_cols)` that takes a two-dimensional array `matrix` and an integer `num_of_cols` as input. The function should print the elements of the matrix column-wise up to `num_of_cols` columns. If `num_of_cols` exceeds the number of columns in the matrix, return an error message.
"""

def print_columns(matrix, num_of_cols):
    if num_of_cols > len(matrix[0]):
        return "Error: The specified number of columns exceeds the number of columns in the matrix."
    else:
        for col in range(num_of_cols):
            for row in matrix:
                print(row[col])