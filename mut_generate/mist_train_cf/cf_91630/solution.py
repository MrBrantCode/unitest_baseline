"""
QUESTION:
Write a function called `fibonacci` that returns the kth element in the Fibonacci sequence with a time complexity of O(log n). The input to the function will be an integer k, and the function should return the kth Fibonacci number. The Fibonacci sequence is defined as F(n) = F(n-1) + F(n-2), with base cases F(0) = 0 and F(1) = 0 or F(1) = 1. The function should handle invalid inputs (k <= 0) by returning None or raising an exception.
"""

def fibonacci(k):
    def multiply_matrix(a, b):
        c = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for l in range(2):
                    c[i][j] += a[i][l] * b[l][j]
        return c

    def power_matrix(matrix, n):
        if n == 0 or n == 1:
            return matrix
        half_power = power_matrix(matrix, n // 2)
        result = multiply_matrix(half_power, half_power)
        if n % 2 == 1:
            result = multiply_matrix(result, matrix)
        return result

    if k <= 0:
        return None
    if k == 1:
        return 0
    matrix = [[1, 1], [1, 0]]
    matrix_power = power_matrix(matrix, k - 1)
    return matrix_power[0][0]