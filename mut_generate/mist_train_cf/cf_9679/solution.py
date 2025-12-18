"""
QUESTION:
Write a function `matrix_power` that takes a 2x2 matrix and a positive integer `n` as inputs and returns the `n`th power of the matrix using exponentiation by squaring. Then use this function to calculate the `n`th Fibonacci number, where `n` is a non-negative integer, by raising a specific 2x2 matrix to the power of `n-1` and returning the top row of the resulting matrix. The matrix should be `[[1, 1], [1, 0]]`.
"""

def matrix_power(matrix, n):
    # Base case: return the matrix itself if n is 1
    if n == 1:
        return matrix
    
    # Recursive case: calculate matrix power using exponentiation by squaring
    half = matrix_power(matrix, n // 2)
    result = matrix_multiply(half, half)

    # Multiply by the original matrix if n is odd
    if n % 2 == 1:
        result = matrix_multiply(result, matrix)

    return result

def matrix_multiply(matrix1, matrix2):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result