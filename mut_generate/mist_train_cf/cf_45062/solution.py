"""
QUESTION:
Create a function `is_prime(n)` that takes an integer `n` as input and returns `True` if `n` is a prime number and `False` otherwise. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2):
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True