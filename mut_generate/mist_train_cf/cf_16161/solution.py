"""
QUESTION:
Create a function that checks if the variable `x` is a prime number and the variable `y` is a perfect square. The function should take two parameters `x` and `y`. It should return `True` if `x` is a prime number and `y` is a perfect square, and `False` otherwise. Assume that `x` and `y` are non-negative integers.
"""

import math

def check_prime_and_perfect_square(x, y):
    """
    Check if x is a prime number and y is a perfect square.

    Args:
        x (int): The number to check for primality.
        y (int): The number to check for perfect square.

    Returns:
        bool: True if x is a prime number and y is a perfect square, False otherwise.
    """
    # Check if x is a prime number
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False

    # Check if y is a perfect square
    square_root = math.isqrt(y)
    return square_root * square_root == y