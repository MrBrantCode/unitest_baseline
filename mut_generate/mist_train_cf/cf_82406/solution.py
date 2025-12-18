"""
QUESTION:
Implement a function `primes_in_range(n, m)` that takes two positive integers `n` and `m`, and returns a list of prime numbers between `n` and `m` inclusive. The function should be optimized to check the divisibility of numbers only up to their square root.
"""

import math

def primes_in_range(n, m):
    if n < 2: 
        n = 2

    primes = []
    for potential_prime in range(n, m + 1):
        is_prime = True
        for num in range(2, math.isqrt(potential_prime) + 1):
            if potential_prime % num == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(potential_prime)
    return primes