"""
QUESTION:
Write a function `multiply_matrices(matrix1, matrix2)` that takes two matrices represented as 2D lists in row-major order and returns their product. The function should raise an exception if the matrices have incompatible dimensions, contain elements of different data types, are not valid (i.e., all rows do not have the same number of columns), or contain complex numbers. If either matrix is empty, the function should return an empty matrix.
"""

def multiply_matrices(matrix1, matrix2):
    # Check if either matrix is empty
    if not matrix1 or not matrix2:
        return []
    
    # Check if the matrices have compatible dimensions
    if len(matrix1[0]) != len(matrix2):
        raise Exception("Incompatible dimensions")
    
    # Check if the matrices contain elements of different data types
    if any(type(element) != type(matrix1[0][0]) for row in matrix1 for element in row) or \
       any(type(element) != type(matrix2[0][0]) for row in matrix2 for element in row):
        raise Exception("Mismatched data types")
    
    # Check if the matrices are valid
    if any(len(row) != len(matrix1[0]) for row in matrix1) or \
       any(len(row) != len(matrix2[0]) for row in matrix2):
        raise Exception("Invalid matrices")
    
    # Check if the matrices contain complex numbers
    if any(isinstance(element, complex) for row in matrix1 for element in row) or \
       any(isinstance(element, complex) for row in matrix2 for element in row):
        raise Exception("Unsupported operation")
    
    # Multiply the matrices
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            element = 0
            for k in range(len(matrix1[0])):
                element += matrix1[i][k] * matrix2[k][j]
            row.append(element)
        result.append(row)
    
    return result