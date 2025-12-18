"""
QUESTION:
Write a function `multiply_matrices(matrix_a, matrix_b)` that takes two matrices as input and returns their product. The input matrices are represented as lists of lists in Python, where each inner list represents a row in the matrix. The function should first check if the number of columns in `matrix_a` is equal to the number of rows in `matrix_b`. If not, it should return an error message. Otherwise, it should return the resulting matrix of the multiplication.
"""

def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])

    if cols_a != rows_b:
        return "Cannot multiply the matrices. Number of columns in Matrix A must be equal to the number of rows in Matrix B."

    result = [[0] * cols_b for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return result