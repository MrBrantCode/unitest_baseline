"""
QUESTION:
Create a function `is_prime(n)` that determines whether a given integer `n` is prime or not. The function should return `True` if `n` is prime and `False` otherwise. The input `n` will be a non-negative integer.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True