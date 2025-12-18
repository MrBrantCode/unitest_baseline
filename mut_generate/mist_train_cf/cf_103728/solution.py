"""
QUESTION:
Write a function `add_matrices` that takes a square matrix `matrix1` and an identity matrix `matrix2` of the same size as parameters. The function should return the result of adding the two matrices together, where the addition operation is performed element-wise. Assume that the input matrices are valid and can be added together.
"""

def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result