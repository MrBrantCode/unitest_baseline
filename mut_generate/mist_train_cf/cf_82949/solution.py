"""
QUESTION:
Create a function `is_prime(n)` that determines if the provided integer `n` is prime or not. The function should return `True` if `n` is prime and `False` otherwise. The function should be efficient and only check divisibility up to the square root of `n`. The input `n` will be a positive integer.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n%2 == 0 or n%3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n%i == 0 or n%(i+2) == 0:
            return False
        i += 6
    return True