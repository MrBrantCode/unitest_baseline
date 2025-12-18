"""
QUESTION:
Given a positive integer n, generate a list of tuples of the form (x, n/x) where x is a prime number that divides n. If n is not divisible by any prime number, return an empty list.

The function should be named `prime_factor_tuples` and should take in an integer n and return a list of tuples. The input integer n is restricted to the range 1 <= n <= 10^6.
"""

import math

def prime_factor_tuples(n):
    """
    Generate a list of tuples of the form (x, n/x) where x is a prime number that divides n.

    Args:
        n (int): A positive integer.

    Returns:
        list: A list of tuples.
    """
    result = []
    for x in range(2, int(math.sqrt(n)) + 1):
        if n % x == 0 and is_prime(x):
            result.append((x, n // x))
    if is_prime(n):
        result.append((n, 1))
    return result

def is_prime(num):
    """
    Check if a number is prime.

    Args:
        num (int): A positive integer.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True