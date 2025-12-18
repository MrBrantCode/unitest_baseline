"""
QUESTION:
Write a function `is_prime(n)` that returns `True` if a number `n` is prime and `False` otherwise, and use it to generate a list of prime numbers from 0 to 100, excluding 2 and 5. The function should not include 2 and 5 in the output list.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True