"""
QUESTION:
Create a function called `add_matrices` that takes two 2D lists (matrices) as input. The function should return a new 2D list that is the sum of the input matrices. The input matrices must have the same number of rows and columns. If the input matrices do not meet this requirement, the function should return an error message.
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