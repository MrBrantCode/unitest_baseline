"""
QUESTION:
Write a function `fibonacci(n)` that generates the nth Fibonacci number using dynamic programming, with a time complexity of O(log n). The Fibonacci sequence is defined as a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1. The function should return the nth Fibonacci number for a given integer `n`, where `n >= 0`.
"""

def fibonacci(n):
    def multiply_matrix(a, b):
        c = [[0, 0], [0, 0]]
        c[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0]
        c[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1]
        c[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0]
        c[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1]
        return c

    def power_matrix(a, n):
        if n == 0:
            return [[1, 0], [0, 1]]
        if n % 2 == 0:
            sqrt = power_matrix(a, n // 2)
            return multiply_matrix(sqrt, sqrt)
        else:
            sqrt = power_matrix(a, (n - 1) // 2)
            return multiply_matrix(multiply_matrix(sqrt, sqrt), a)

    if n <= 0:
        return 0
    fib_matrix = [[1, 1], [1, 0]]
    result_matrix = power_matrix(fib_matrix, n - 1)
    return result_matrix[0][0]