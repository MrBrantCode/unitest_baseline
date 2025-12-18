"""
QUESTION:
Create a function named `matrix_power` that takes as input a square matrix of size n x n and a positive integer power, and returns the result of raising the matrix to that power. The function should not use any external libraries and should handle matrix multiplication internally.
"""

def matrix_power(matrix, power):
    n = len(matrix)
    result = matrix
    
    # Perform the matrix multiplication power-1 times
    for _ in range(1, power):
        result = matrix_multiplication(result, matrix, n)
        
    return result


def matrix_multiplication(A, B, n):
    # Creating an empty matrix
    res = [[0 for x in range(n)] for y in range(n)]
    
    # Multiplies two matrices A[x][y] and B[y][z] and stores results in res[x][z]
    for x in range(n):
        for y in range(n):
            res[x][y] = 0
            for z in range(n):
                res[x][y] += A[x][z] * B[z][y]
                
    return res