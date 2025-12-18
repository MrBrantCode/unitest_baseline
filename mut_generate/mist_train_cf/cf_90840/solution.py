"""
QUESTION:
Write a function `multiply_matrices(matrix1, matrix2)` that takes two 2D lists `matrix1` and `matrix2` representing matrices and returns their product matrix if the number of columns in `matrix1` is equal to the number of rows in `matrix2`. If the matrices cannot be multiplied, return `None`. Assume the input matrices are valid (i.e., they are rectangular and contain only numbers).
"""

def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        return None
    
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result