"""
QUESTION:
Design a function called `matrix_properties` that takes a 2D list `matrix` as input. The function should return a tuple containing four values: the number of rows in the matrix, the number of columns, the sum of the diagonal elements, and a boolean indicating whether the matrix is square (i.e., the number of rows equals the number of columns).
"""

def matrix_properties(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0
    diagonal_sum = sum(matrix[i][i] for i in range(min(rows, cols)))
    is_square = rows == cols
    return rows, cols, diagonal_sum, is_square