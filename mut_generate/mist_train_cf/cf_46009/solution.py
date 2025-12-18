"""
QUESTION:
Create a function called `is_prime` that takes an integer `n` as input, and returns `True` if `n` is a prime number, and `False` otherwise. The function should be able to handle integers up to 10^6.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True