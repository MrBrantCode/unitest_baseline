"""
QUESTION:
Calculate the result of raising an n x n matrix to a given power under modulo operation. The function `matrix_power` should take as input the matrix, its dimensions (n), the power to which it should be raised, and the modulo value. The function should perform matrix multiplication and exponentiation in logarithmic time complexity. The matrix is guaranteed to be square.
"""

def matrix_power(matrix, n, power, mod):
    def matrix_multiply(matrix1, matrix2):
        result = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    result[i][j] = (result[i][j] + (matrix1[i][k] * matrix2[k][j]) % mod) % mod
        return result

    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        result[i][i] = 1

    while power > 0:
        if power % 2:
            result = matrix_multiply(result, matrix)
            power -= 1
        else:
            matrix = matrix_multiply(matrix, matrix)
            power //= 2
    return result