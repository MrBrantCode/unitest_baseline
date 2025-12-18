"""
QUESTION:
In this kata you will create a function to check a non-negative input to see if it is a prime number.

The function will take in a number and will return True if it is a prime number and False if it is not.

A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

### Examples
"""

import math

def is_prime(n: int) -> bool:
    """
    Check if a given non-negative integer is a prime number.

    Parameters:
    n (int): The non-negative integer to check for primality.

    Returns:
    bool: True if n is a prime number, False otherwise.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True