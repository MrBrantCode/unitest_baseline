"""
QUESTION:
Implement a function `geometric_mean_of_fibonacci` that calculates the geometric mean of the first `n` elements in the Fibonacci sequence. The function should take an integer `n` as input and return the geometric mean. Assume `n` is a positive integer greater than 1. The geometric mean is calculated by multiplying all the numbers together, then taking the nth root of the product.
"""

import math

def geometric_mean_of_fibonacci(n):
    """
    Calculate the geometric mean of the first n elements in the Fibonacci sequence.

    Args:
        n (int): A positive integer greater than 1.

    Returns:
        float: The geometric mean of the first n elements in the Fibonacci sequence.
    """
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    product = math.prod(sequence)
    return product ** (1.0 / len(sequence))