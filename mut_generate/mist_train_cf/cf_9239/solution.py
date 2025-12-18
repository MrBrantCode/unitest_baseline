"""
QUESTION:
Create a function `multiply_matrices` that takes two n x n matrices represented as two-dimensional lists as input and returns their product as a new n x n matrix. The function should assume that the input matrices are valid for multiplication (i.e., they have the same dimensions).
"""

def multiply_matrices(matrix1, matrix2):
    n = len(matrix1)
    result = [[0 for x in range(n)] for y in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result