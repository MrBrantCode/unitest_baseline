"""
QUESTION:
Construct a function `is_prime(n)` that determines whether a given integer `n` is a prime number or not. The function should return `True` if `n` is prime and `False` otherwise, with the constraint that it must check for divisibility only up to the square root of `n`.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n == 2: 
        return True
    if n % 2 == 0: 
        return False
    max_div = int(n**0.5) + 1
    for divisor in range(3, max_div, 2):
        if n % divisor == 0:
            return False
    return True