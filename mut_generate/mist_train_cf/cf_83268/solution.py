"""
QUESTION:
Write a function `is_prime(n)` that determines whether a given number `n` is prime. The function should return `True` if `n` is prime and `False` otherwise. The input `n` is a positive integer.
"""

def is_prime(n):
    """Returns True if n is a prime number, False otherwise."""
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True