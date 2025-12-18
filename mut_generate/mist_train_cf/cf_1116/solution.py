"""
QUESTION:
Write a function named `is_prime` to determine whether a given positive integer is prime and not a perfect square. The function should return True if the number is prime and not a perfect square, and False otherwise. Assume that the input will be a positive integer greater than or equal to 1.
"""

import math

def is_prime(n):
    """
    Determine whether a given positive integer is prime and not a perfect square.

    Args:
    n (int): A positive integer greater than or equal to 1.

    Returns:
    bool: True if the number is prime and not a perfect square, False otherwise.
    """
    if n < 2:
        return False
    is_prime = True
    divisor = 2
    while divisor <= math.sqrt(n):
        if n % divisor == 0:
            is_prime = False
            break
        divisor += 1
    if is_prime:
        sqrt = math.sqrt(n)
        if sqrt.is_integer():
            return False
        else:
            return True
    else:
        return False