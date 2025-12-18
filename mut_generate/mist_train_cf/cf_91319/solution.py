"""
QUESTION:
Write a function `multiply_matrices(matrix_a, matrix_b)` that takes two 2D lists `matrix_a` and `matrix_b` as input and returns their product. The function should check if the multiplication is possible (i.e., the number of columns in `matrix_a` is equal to the number of rows in `matrix_b`) and return an error message if it's not. If the multiplication is possible, the function should return a new 2D list representing the product of `matrix_a` and `matrix_b`.
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