"""
QUESTION:
Create a function called `multiply_matrices` that takes two square matrices as parameters. The first matrix is any square matrix, and the second matrix is an identity matrix of the same size. The function should only accept matrices with dimensions between 2 and 10 (inclusive). The function should return the result of multiplying the two matrices together, with the constraint that all elements in the resulting matrix must be prime numbers.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def multiply_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return "Matrices must have the same size."
    n = len(matrix1)
    if n < 2 or n > 10:
        return "Matrix size must be between 2 and 10 (inclusive)."
    
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
            if not is_prime(result[i][j]):
                return "Resulting matrix should only contain prime numbers."
    
    return result