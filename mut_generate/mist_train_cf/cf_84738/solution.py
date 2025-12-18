"""
QUESTION:
Create a function `fibonacci(n, mod)` that generates the nth Fibonacci number using matrix exponentiation and modular arithmetic. The function should take two parameters: `n`, the index of the Fibonacci number, and `mod`, the modulus for the modular arithmetic (default value is 10^9 + 7). The function should return the nth Fibonacci number modulo `mod`.
"""

def fibonacci(n, mod=10**9 + 7):
    def matrix_mult(a, b, mod):
        c = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    c[i][j] += a[i][k] * b[k][j]
                c[i][j] %= mod
        return c

    def matrix_exp(m, n, mod):
        if n == 1:
            return m
        elif n % 2 == 0:
            temp = matrix_exp(m, n // 2, mod)
            return matrix_mult(temp, temp, mod)
        else:
            return matrix_mult(m, matrix_exp(m, n - 1, mod), mod)

    if n <= 1:
        return n
    initial_matrix = [[1, 1], [1, 0]]
    result_matrix = matrix_exp(initial_matrix, n - 1, mod)
    return result_matrix[0][0]