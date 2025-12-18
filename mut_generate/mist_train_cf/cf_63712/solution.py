"""
QUESTION:
Write a function `matrix_power(matrix, power, n)` that calculates the exponentiation of an n x n matrix `matrix` by a given `power` using the method of Exponentiation by Squaring. The function should not use any external libraries and should be efficient for large matrices and powers. The input `matrix` is a 2D list of size n x n, and `power` is a non-negative integer.
"""

def matrix_power(matrix, power, n):
    def matmul(A,B,n):
        return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    def identity(n):
        return [[1 if i==j else 0 for j in range(n)] for i in range(n)]
    
    result = identity(n)
    while power > 0:
        if power % 2 == 1:
            result = matmul(result, matrix, n)
        matrix = matmul(matrix, matrix, n)
        power //= 2
    return result