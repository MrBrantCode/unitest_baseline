"""
QUESTION:
Write a function `is_prime(n)` that checks if a number `n` is prime, and use it to calculate the sum of all prime numbers between 4 and 1000 (inclusive).
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True