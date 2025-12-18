"""
QUESTION:
Compose a function called `fibonacci` that generates the nth Fibonacci number without using recursive functions or loops like for/while. The function should be able to handle large ordinal numbers efficiently and return previously calculated Fibonacci numbers in O(1) time.
"""

import numpy as np

def fibonacci(n, fibs={0: 0, 1: 1}):
    def matrix_power(matrix, n):
        if n <= 0:
            return np.eye(2, dtype=int)
        elif n % 2 == 0:
            return matrix_power(np.dot(matrix, matrix), n // 2)
        else:
            return np.dot(matrix, matrix_power(matrix, n - 1))

    if n not in fibs:
        matrix = np.array([[1, 1], [1, 0]], dtype=object)
        matrix = matrix_power(matrix, n - 1)
        fibs[n] = int(matrix[0, 0])
    return fibs[n]