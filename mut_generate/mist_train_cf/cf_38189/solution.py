"""
QUESTION:
Create a function `is_prime(n)` that takes an integer `n` as input and returns a boolean value indicating whether `n` is a prime number or not. If `n` is a prime number (a natural number greater than 1 with no positive divisors other than 1 and itself), the function should return `True`. If `n` is not prime, the function should return `False`. If `n` is not a positive integer, the function should also return `False`.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True