"""
QUESTION:
Create a function named `fib` that takes an integer `n` as input and returns the nth Fibonacci number, with a time complexity of O(log(n)). The function should handle cases where `n` is 0 or 1, and return the correct Fibonacci number for `n > 1`.
"""

def fib(n):
    def matrix_mult(a, b):
        result = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    result[i][j] += a[i][k] * b[k][j]
        return result

    def matrix_power(matrix, n):
        if n == 0:
            return [[1, 0], [0, 1]]
        if n == 1:
            return matrix

        if n % 2 == 0:  # Even power
            half_power = matrix_power(matrix, n // 2)
            return matrix_mult(half_power, half_power)
        else:  # Odd power
            return matrix_mult(matrix, matrix_power(matrix, n - 1))

    if n <= 1:
        return n
    matrix = [[1, 1], [1, 0]]
    result = matrix_power(matrix, n - 1)
    return result[0][0]