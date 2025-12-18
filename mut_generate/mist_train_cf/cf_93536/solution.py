"""
QUESTION:
Write a function named `fibonacci` that generates the nth Fibonacci number. The function should use dynamic programming and have a time complexity of O(log n).
"""

def fibonacci(n):
    def multiply_matrix(a, b):
        # Multiplies two matrices
        c = [[0, 0], [0, 0]]
        c[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0]
        c[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1]
        c[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0]
        c[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1]
        return c

    def power_matrix(a, n):
        # Raises a matrix to the power of n
        if n == 0:
            return [[1, 0], [0, 1]]  # Identity matrix
        if n % 2 == 0:
            sqrt = power_matrix(a, n // 2)
            return multiply_matrix(sqrt, sqrt)
        else:
            sqrt = power_matrix(a, (n - 1) // 2)
            return multiply_matrix(multiply_matrix(sqrt, sqrt), a)

    if n <= 0:
        return 0
    fib_matrix = [[1, 1], [1, 0]]  # Fibonacci matrix
    result_matrix = power_matrix(fib_matrix, n - 1)
    return result_matrix[0][0]