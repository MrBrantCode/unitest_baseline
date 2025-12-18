"""
QUESTION:
Write a function named `prime_composite_ascii_sum` that takes two strings `str1` and `str2` as input and returns `True` if the sum of ASCII values of characters in `str1` is a prime number and the sum of ASCII values of characters in `str2` is a composite number. Otherwise, it should return `False`.
"""

import math

def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def is_composite(num):
    """Check if a number is composite."""
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return True
    return False

def prime_composite_ascii_sum(str1, str2):
    """
    Check if the sum of ASCII values of characters in str1 is a prime number
    and the sum of ASCII values of characters in str2 is a composite number.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        bool: True if the conditions are met, False otherwise.
    """
    sum1 = sum(ord(char) for char in str1)
    sum2 = sum(ord(char) for char in str2)

    return is_prime(sum1) and is_composite(sum2)