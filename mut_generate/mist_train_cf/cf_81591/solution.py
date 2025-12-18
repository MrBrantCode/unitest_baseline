"""
QUESTION:
Create a function named `is_prime(n)` that determines if a given integer `n` is a prime number. The function should return `True` if `n` is prime, and `False` otherwise. The function should be able to handle any positive integer input.
"""

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i += 6
    return True