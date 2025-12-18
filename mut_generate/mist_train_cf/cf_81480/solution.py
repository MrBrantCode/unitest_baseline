"""
QUESTION:
Create a function called `is_prime(n)` that determines whether a given integer `n` is prime or not, returning `True` if it is prime and `False` otherwise. The function should work for all integers and handle cases where `n` is less than 2.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True