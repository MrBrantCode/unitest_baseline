"""
QUESTION:
Write a function `fibonacci(n)` that calculates the Nth Fibonacci number. The function should have a time complexity of O(logN). The input `n` is a positive integer.
"""

def fibonacci(n):
    def matrix_multiply(a, b):
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
        half = matrix_power(matrix, n // 2)
        if n % 2 == 0:
            return matrix_multiply(half, half)
        else:
            return matrix_multiply(matrix_multiply(half, half), matrix)

    if n <= 0:
        return "Invalid input"
    if n == 1:
        return 0
    fib_matrix = [[1, 1], [1, 0]]
    fib_matrix_power = matrix_power(fib_matrix, n - 1)
    return fib_matrix_power[0][0]