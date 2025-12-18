"""
QUESTION:
Implement a function `matrix_addition(matrix1, matrix2)` that adds two sparse matrices `matrix1` and `matrix2`. The function should return the result matrix. 

The function must handle matrices of different sizes and return "Matrices must have the same size" if they do not match. It should also validate the input matrices, returning "Invalid matrices" if they contain non-numerical values or have incorrect dimensions. Additionally, the function should check for symmetric matrices, returning "Matrices are symmetric" if both matrices are square and have symmetric elements.

The function should have a time complexity of O(n), where n represents the number of non-zero elements in the matrices, and a space complexity of O(m + n), where m represents the number of rows in the matrices and n represents the number of columns.
"""

def matrix_addition(matrix1, matrix2):
    # Check if matrices have the same size
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return "Matrices must have the same size"

    # Check if matrices are valid
    for row in matrix1 + matrix2:
        for element in row:
            if not isinstance(element, (int, float)):
                return "Invalid matrices"

    # Check if matrices are symmetric
    if len(matrix1) == len(matrix1[0]) == len(matrix2) == len(matrix2[0]):
        for i in range(len(matrix1)):
            for j in range(i + 1, len(matrix1[0])):
                if matrix1[i][j] != matrix1[j][i] or matrix2[i][j] != matrix2[j][i]:
                    break
            else:
                continue
            break
        else:
            return "Matrices are symmetric"

    # Perform matrix addition
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    return result