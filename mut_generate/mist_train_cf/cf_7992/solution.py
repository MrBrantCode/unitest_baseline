"""
QUESTION:
Create a function named `is_prime()` that takes a number as input and returns `True` if it is prime, `False` otherwise. Using this function, print all prime numbers from 1 to a given positive integer `n` (where `n` is greater than or equal to 10) separated by a space.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True