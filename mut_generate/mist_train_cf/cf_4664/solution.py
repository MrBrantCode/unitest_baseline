"""
QUESTION:
Implement a function called `matrix_addition` that takes two 2D arrays (matrices) as input and returns their sum as a 2D array. The function should first check if the input matrices are valid (containing only numerical values and having the same dimensions) and have the same size (number of rows and columns). If not, it should return an error message "Matrices must have the same size" or "Invalid matrices". If the matrices are valid and of the same size, the function should then check if they are symmetric. If they are symmetric, it should return a message "Matrices are symmetric". Otherwise, it should perform the matrix addition and return the result. The time complexity should be O(n), where n is the total number of non-zero elements in the matrices, and the space complexity should be O(m + n), where m is the number of rows and n is the number of columns.
"""

def matrix_addition(matrix1, matrix2):
    # Check if matrices have the same size
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return "Matrices must have the same size"

    # Check if matrices are valid
    if not is_valid_matrix(matrix1) or not is_valid_matrix(matrix2):
        return "Invalid matrices"

    # Check if matrices are symmetric
    if is_symmetric_matrix(matrix1) and is_symmetric_matrix(matrix2):
        return "Matrices are symmetric"

    # Perform matrix addition
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result


def is_valid_matrix(matrix):
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                return False
    return True


def is_symmetric_matrix(matrix):
    if len(matrix) != len(matrix[0]):
        return False

    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix[0])):
            if matrix[i][j] != matrix[j][i]:
                return False

    return True