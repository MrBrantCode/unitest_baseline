"""
QUESTION:
Design a function `is_prime(n)` that determines whether a given integer `n` is a prime number or not. The function should return `True` if `n` is prime and `False` otherwise. The input `n` is an integer greater than 0.
"""

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True