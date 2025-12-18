"""
QUESTION:
Create a function named `is_prime` that takes an integer `n` as input and returns a boolean indicating whether `n` is a prime number or not. The function should return `True` if `n` is prime and `False` otherwise. Note that the function should be optimized for performance by stopping the check for divisors at the square root of `n` and skipping even divisors after 2.
"""

def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3: 
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True