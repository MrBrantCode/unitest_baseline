"""
QUESTION:
Write a function `is_prime_perfect_square(x: int, y: int) -> bool` that takes two positive integers `x` and `y` and returns `True` if `x` is a prime number and `y` is a perfect square, and `False` otherwise. The function should have a time complexity of O(sqrt(x)) and a space complexity of O(1), and be implemented using an `if` statement.
"""

import math

def is_prime_perfect_square(x: int, y: int) -> bool:
    """
    Checks if x is a prime number and y is a perfect square.

    Args:
        x (int): The number to check for primality.
        y (int): The number to check for perfect square.

    Returns:
        bool: True if x is prime and y is a perfect square, False otherwise.
    """
    
    # Check if y is a perfect square
    if math.sqrt(y) != int(math.sqrt(y)):
        return False
    
    # Check if x is prime
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
            
    return True