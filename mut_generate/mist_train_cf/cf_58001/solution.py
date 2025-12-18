"""
QUESTION:
Write a function `is_prime(n)` that determines whether a given integer `n` is prime. The function should return `True` if `n` is prime and `False` otherwise. The function should have the same behavior as the original but with improved efficiency. It should only check divisibility up to the square root of `n`.
"""

def entrance(n):
    """Returns true for prime integers, false for non-prime integers."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Start from 3 and step through odd numbers up to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True