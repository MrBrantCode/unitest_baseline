"""
QUESTION:
Write a function `is_prime(n)` that takes a positive integer `n` greater than 1 as input and returns `True` if `n` is a prime number and `False` otherwise.
"""

def entrance(n):
    # Check if n is divisible by any number from 2 to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True