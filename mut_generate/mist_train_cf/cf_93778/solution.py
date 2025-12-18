"""
QUESTION:
Write a function `multiply_matrices(matrix1, matrix2)` that takes two 2D lists (matrices) as input and returns their product. The function should first check if the number of columns in `matrix1` is equal to the number of rows in `matrix2`, and if not, return an error message. If the matrices can be multiplied, the function should create a result matrix with the correct dimensions and fill it with the product of the corresponding elements from `matrix1` and `matrix2`.
"""

def multiply_matrices(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    # check if the number of columns in matrix1 is equal to the number of rows in matrix2
    if cols1 != rows2:
        return "Cannot multiply matrices. Number of columns in matrix1 should be equal to the number of rows in matrix2."

    # create a result matrix with dimensions n x p, where p is the number of columns in matrix2
    result = [[0] * cols2 for _ in range(rows1)]

    # multiply the matrices
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result