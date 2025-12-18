"""
QUESTION:
Write a function `add_matrices` that takes two matrices as input and returns their sum, provided that both matrices have the same number of rows and columns. If the matrices do not have the same dimensions, the function should return an error message. The function should be able to handle matrices of any size.
"""

def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    columns = len(matrix1[0])

    if rows != len(matrix2) or columns != len(matrix2[0]):
        return "Matrices must have the same number of rows and columns"

    result = [[0 for _ in range(columns)] for _ in range(rows)]

    for i in range(rows):
        for j in range(columns):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

    return result