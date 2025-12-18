"""
QUESTION:
Create a function `is_prime(n)` to check whether a given number `n` is prime. The function should return `True` if `n` is prime and `False` otherwise. A prime number is a number that has exactly two distinct divisors: 1 and itself.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True