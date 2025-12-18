"""
QUESTION:
Create a function `is_prime(n)` that checks whether a given number `n` is prime. The function should return `True` if `n` is prime and `False` otherwise. Use this function to generate a list of all prime numbers from 1 to 100.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True