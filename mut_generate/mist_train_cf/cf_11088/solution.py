"""
QUESTION:
Write a function `is_prime(n)` that takes a positive integer `n` as input and returns `True` if `n` is a prime number and `False` otherwise.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True