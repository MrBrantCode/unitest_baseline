"""
QUESTION:
Write a function `multiply_matrices(matrix1, matrix2)` that multiplies two matrices represented as two-dimensional lists. The function should first check if the number of columns in `matrix1` is equal to the number of rows in `matrix2`. If they are not equal, return an error message. Otherwise, return the result of the matrix multiplication. The dimensions of `matrix1` should be n x m and the dimensions of `matrix2` should be m x p.
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