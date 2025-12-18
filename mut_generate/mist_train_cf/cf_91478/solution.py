"""
QUESTION:
Write a function `is_prime(n)` that takes an integer `n` as input and returns `True` if `n` is a prime number not divisible by 2 or 3, and `False` otherwise. The function should handle integers between 1 and 100.
"""

def entrance(n):
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