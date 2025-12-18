"""
QUESTION:
Create a function named `is_prime` that takes an integer `n` as input and returns `True` if the number is prime and `False` otherwise. The function should handle integers greater than 1.
"""

import math
def entrance(n):
    """
    This function checks if a number is prime.
    :param n: int -- the number to check.
    :return: bool -- True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:  # Eliminating divisible by 2 and 3
        return False
    i = 5
    while i * i <= n:  # Check up to the square root of n
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True