"""
QUESTION:
Write a function named `is_prime(n)` that takes an integer `n` as input and returns `True` if `n` is a prime number, otherwise returns `False`. Then, use this function to output all prime numbers between 1 and 10 (inclusive).
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            return False
    return True