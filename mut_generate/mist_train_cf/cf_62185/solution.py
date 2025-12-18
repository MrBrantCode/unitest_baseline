"""
QUESTION:
Design a function called `is_prime(n)` that checks if a number `n` is prime. The function should return `True` if the number is prime, and `False` otherwise. The function should work for all positive integers.
"""

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True