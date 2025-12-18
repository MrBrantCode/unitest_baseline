"""
QUESTION:
Write two functions: `fibonacci(n)` and `is_fibonacci(n)`. 

Function `fibonacci(n)` should return the nth Fibonacci number. This function must have a runtime complexity of O(log n).

Function `is_fibonacci(n)` should return True if the given number `n` is a Fibonacci number and False otherwise. This function must have a runtime complexity of O(1).
"""

import numpy as np
import math

def fibonacci(n):
    # Base case
    if n <= 1:
        return n
    
    # Define the matrix M
    M = np.array([[1, 1], [1, 0]])
    
    # Calculate M^(n-1)
    result = np.linalg.matrix_power(M, n-1)
    
    # Multiply the result by [F(1), F(0)]
    fib_vector = np.array([[1], [0]])
    fib_result = np.dot(result, fib_vector)
    
    return fib_result[0][0]

def is_fibonacci(n):
    return math.isqrt(5 * n**2 + 4) ** 2 == 5 * n**2 + 4 or math.isqrt(5 * n**2 - 4) ** 2 == 5 * n**2 - 4