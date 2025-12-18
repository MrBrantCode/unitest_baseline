"""
QUESTION:
Write a function `multiply_matrices(matrix1, matrix2)` that multiplies two matrices. The function should take two parameters, `matrix1` and `matrix2`, both of which are 2D lists of integers representing matrices. The number of columns in `matrix1` must be equal to the number of rows in `matrix2`. The function should return a new 2D list representing the product of `matrix1` and `matrix2`, or an empty list if either input matrix is empty. The resulting matrix should have the same number of rows as `matrix1` and the same number of columns as `matrix2`.
"""

def multiply_matrices(matrix1, matrix2):
    # Check if either matrix is empty
    if not matrix1 or not matrix2:
        return []
    
    # Check if number of columns in matrix1 is equal to number of rows in matrix2
    if len(matrix1[0]) != len(matrix2):
        return []
    
    # Initialize an empty result matrix with the same number of rows as matrix1 and
    # the same number of columns as matrix2
    result = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]
    
    # Perform matrix multiplication
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result