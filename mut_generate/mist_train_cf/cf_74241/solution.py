"""
QUESTION:
Create a function named `is_prime(n)` that determines whether a given integer `n` is a prime number. The function should return `True` if `n` is prime and `False` otherwise. Assume that the input will be a positive integer. The function should be optimized to minimize unnecessary computations.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5)  
    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return False
    return True