"""
QUESTION:
Create a function `isprime(n)` that determines if a given number `n` is a prime number or not. If `n` is not a prime number, the function should also return the two smallest prime factors of `n`. The function should return a boolean value indicating whether `n` is prime, and if not, return the two smallest prime factors.
"""

import math

def isprime(n):
    if n <= 1:
        return False, None
    if n <= 3:
        return True, None
    if n % 2 == 0 or n % 3 == 0:
        return False, 2 if n % 2 == 0 else 3

    i = 5
    while i * i <= n:
        if n % i== 0 or n % (i + 2) == 0:
            return False, i if n % i == 0 else i + 2
        i += 6

    return True, None