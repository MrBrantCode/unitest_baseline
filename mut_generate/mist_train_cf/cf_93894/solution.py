"""
QUESTION:
Write a function `multiply_matrices(matrix1, matrix2)` that takes two matrices as input, multiplies them, and returns the result. The function should handle the following conditions:

*   The number of columns in `matrix1` must be equal to the number of rows in `matrix2`. If not, raise an exception with the message "Incompatible dimensions: number of columns in the first matrix must be equal to the number of rows in the second matrix".
*   The matrices must contain elements of the same data type. If not, raise an exception with the message "Mismatched data types in matrices".
*   The matrices must be valid, meaning all rows have the same number of columns. If not, raise an exception with the message "Invalid matrices: all rows must have the same number of columns".
*   If either matrix is empty, return an empty matrix.
"""

def multiply_matrices(matrix1, matrix2):
    # Check if matrices are empty
    if not matrix1 or not matrix2:
        return []

    # Check if matrices have incompatible dimensions
    if len(matrix1[0]) != len(matrix2):
        raise Exception("Incompatible dimensions: number of columns in the first matrix must be equal to the number of rows in the second matrix")

    # Check if matrices contain elements of different data types
    matrix1_type = type(matrix1[0][0])
    matrix2_type = type(matrix2[0][0])
    if any(type(elem) != matrix1_type for row in matrix1 for elem in row) or any(type(elem) != matrix2_type for row in matrix2 for elem in row):
        raise Exception("Mismatched data types in matrices")

    # Check if matrices are valid matrices
    matrix1_cols = len(matrix1[0])
    if any(len(row) != matrix1_cols for row in matrix1) or any(len(row) != len(matrix2[0]) for row in matrix2):
        raise Exception("Invalid matrices: all rows must have the same number of columns")

    # Perform matrix multiplication
    result = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result