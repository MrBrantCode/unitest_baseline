"""
QUESTION:
Write a function `is_prime(n)` that takes an integer `n` as input and returns `True` if `n` is a prime number and `False` otherwise. Then, use this function to calculate the sum and product of all prime numbers between 1 and 100 (inclusive).
"""

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True