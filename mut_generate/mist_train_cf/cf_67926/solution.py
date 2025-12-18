"""
QUESTION:
Write a function `fibonacci(n)` to calculate the nth number in the Fibonacci sequence. The function should be optimized for efficiency in terms of time and space complexity, handling arbitrarily large numbers without precision errors.
"""

import numpy as np

def fibonacci(n):
    def matrix_power(matrix, n):
        result = np.eye(2)
        while n > 0:
            if n % 2 == 1:
                result = np.matmul(result, matrix)
            matrix = np.matmul(matrix, matrix)
            n //= 2
        return result

    matrix = np.array([[1, 1], [1, 0]])
    powered_matrix = matrix_power(matrix, n - 1)   
    return powered_matrix[0, 0]