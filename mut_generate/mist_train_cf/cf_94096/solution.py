"""
QUESTION:
Write a function that checks if a given number `x` is a prime number and a given number `y` is a perfect square. The function should return `True` if both conditions are met and `False` otherwise. The function should be able to handle any positive integers `x` and `y`.
"""

import math

def entrance(x, y):
    """
    Checks if x is a prime number and y is a perfect square.
    
    Args:
    x (int): The number to check for primality.
    y (int): The number to check if it's a perfect square.
    
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