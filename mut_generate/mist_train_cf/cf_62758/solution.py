"""
QUESTION:
Create a function `fibonacci` that calculates the `n`-th digit in an adjusted Fibonacci series, where each digit is the residual value of the original Fibonacci digit and a given dynamic input `y`. The function should be capable of handling substantial values of `n` (up to 1,000,000). The function should take two parameters: `n`, the position of the digit in the series, and `y`, the dynamic input used to calculate the residual value.
"""

import numpy as np

def fibonacci(n, y):
    def multiply_matrices(a, b, mod):
        return np.vectorize(lambda x: x%mod)(np.dot(a, b))

    def power(matrix, n, mod):
        if n == 0:
            return np.array([[1, 0], [0, 1]])
        elif n == 1:
            return matrix
        else:
            half_n = power(matrix, n//2, mod)
            if n % 2 == 0:
                return multiply_matrices(half_n, half_n, mod)
            else:
                return multiply_matrices(multiply_matrices(half_n, half_n, mod), matrix, mod)

    initial_matrix = np.array([[1, 1], [1, 0]])
    powered_matrix = power(initial_matrix, n, y)
    return powered_matrix[1, 0]