"""
QUESTION:
Write a function `is_prime(num)` that takes an integer as input and returns a boolean indicating whether the number is prime or not. For numbers 1 to 100, use this function to print the number along with a message stating whether it is a prime number or not. The function should return False for numbers less than or equal to 1 and should only check divisibility up to the square root of the number for efficiency.
"""

import math

def is_prime(num):
    """
    Checks if a number is prime.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False
    return True