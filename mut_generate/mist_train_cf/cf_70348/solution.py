"""
QUESTION:
Create a function called `fibonacci_matrix(n)` that generates an n x n matrix where the elements are the Fibonacci sequence. The matrix is filled in a row-major order. The function should not take any input other than the matrix size `n` and should return the generated matrix.
"""

import numpy as np

def fibonacci_matrix(n):
    """
    Generates an n x n matrix where the elements are the Fibonacci sequence.
    The matrix is filled in a row-major order.

    Parameters:
    n (int): The size of the matrix.

    Returns:
    numpy.ndarray: The generated Fibonacci matrix.
    """
    fibo_numbers = [0, 1]
    for i in range(2, n*n + 1):
        fibo_numbers.append(fibo_numbers[i-1] + fibo_numbers[i-2])

    return np.array(fibo_numbers[1:]).reshape((n, n))