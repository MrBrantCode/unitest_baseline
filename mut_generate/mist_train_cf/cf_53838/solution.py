"""
QUESTION:
Design a function `generate_primes(n)` that generates and lists all prime numbers less than a specified number `n`, where `n` can be either very high (beyond 10^6) or relatively low (less than 10). The function should handle both cases efficiently and accurately.
"""

import math

def generate_primes(n):
    if n<=1:
        return []
    else:
        sieve = [True] * (n+1)
        for x in range(2, int(math.sqrt(n)) + 1):
            if sieve[x]:
                for i in range(x*x, n + 1, x):
                    sieve[i] = False
        return [i for i in range(2, n) if sieve[i]]