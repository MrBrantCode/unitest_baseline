"""
QUESTION:
Implement a function named `matrix_addition` that takes two 2D arrays representing matrices as input. The function should add the two matrices element-wise and return the result. If the matrices are not the same size, the function should return "Matrices must have the same size". If the matrices contain non-numerical values or have incorrect dimensions, the function should return "Invalid matrices". If both matrices are symmetric, the function should return "Matrices are symmetric". The function should have a time complexity of O(n), where n is the number of non-zero elements in the matrices, and a space complexity of O(m + n), where m is the number of rows and n is the number of columns.
"""

def matrix_addition(matrix1, matrix2):
    # Check if matrices are valid
    if not (is_valid_matrix(matrix1) and is_valid_matrix(matrix2)):
        return "Invalid matrices"
    
    # Check if matrices have same size
    if get_matrix_size(matrix1) != get_matrix_size(matrix2):
        return "Matrices must have the same size"

    # Check if matrices are symmetric
    if is_symmetric(matrix1) and is_symmetric(matrix2):
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

def get_matrix_size(matrix):
    return (len(matrix), len(matrix[0]))

def is_symmetric(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    if rows != cols:
        return False
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True