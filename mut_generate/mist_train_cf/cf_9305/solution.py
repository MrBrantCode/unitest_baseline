"""
QUESTION:
Write a function `multiply_matrices(matrix1, matrix2)` that takes two matrices as input and returns their product matrix. The function should first check if the input matrices can be multiplied by comparing the number of columns in the first matrix with the number of rows in the second matrix. If the matrices cannot be multiplied, the function should return `None`. If the matrices can be multiplied, the function should create a result matrix with the appropriate dimensions and perform the matrix multiplication. The function should return the result matrix.
"""

def multiply_matrices(matrix1, matrix2):
    # Checking if the matrices can be multiplied
    if len(matrix1[0]) != len(matrix2):
        return None
    
    # Creating an empty result matrix
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    
    # Multiplying matrices
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result