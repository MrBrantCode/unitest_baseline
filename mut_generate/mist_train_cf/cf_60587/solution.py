"""
QUESTION:
Implement the `is_prime(n)` function to determine whether a given integer `n` is a prime number or not. The function should return `True` for prime numbers and `False` for non-prime numbers. The function should be optimized for performance. Note that the input integer `n` is a positive integer greater than or equal to 1.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True