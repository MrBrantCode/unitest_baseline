"""
QUESTION:
Write a function `is_prime(n)` that determines if a number is prime. Using this function, find the sum of all prime numbers between 1 and 100000. The `is_prime(n)` function should return `True` if the number is prime and `False` otherwise.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True