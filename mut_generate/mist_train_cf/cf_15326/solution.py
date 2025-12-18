"""
QUESTION:
Create a function `is_prime(n)` that checks if a given integer `n` is a prime number using the Sieve of Eratosthenes algorithm. The function should return `True` if `n` is prime, and `False` otherwise. The function should be efficient enough to handle large input numbers.
"""

import math

def is_prime(n):
    if n <= 1:
        return False

    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(math.sqrt(n)) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    return sieve[n]