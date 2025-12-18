"""
QUESTION:
Develop a function called is_prime that takes an integer n as input, where n is greater than or equal to 2, and returns True if the number is prime and False otherwise.
"""

import math

def is_prime(n):
    """
    Checks if a given integer is a prime number or not.

    Args:
        n (int): An integer number greater than or equal to 2.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True