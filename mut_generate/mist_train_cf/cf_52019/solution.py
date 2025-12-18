"""
QUESTION:
Write a function called `fibonacci` that takes an integer `n` as input and returns the `n`-th element of the Fibonacci sequence. The function should handle numbers up to 1000 efficiently and should not use recursion or memoization. The function should also be able to handle large integers without causing overflow.
"""

import numpy as np

def fibonacci(n):
    initial_matrix = np.array([[1,1],[1,0]], dtype=np.int64)
    result = np.eye(len(initial_matrix))

    while n > 0:
        if n % 2 == 1: 
            result = np.dot(result, initial_matrix) % 1000000007
        initial_matrix = np.dot(initial_matrix, initial_matrix) % 1000000007
        n //= 2
    return result[1][0]