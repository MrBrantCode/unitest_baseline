"""
QUESTION:
Create a function `generate_primes(n)` that generates all prime numbers less than a given number `n`. The function should be able to handle inputs up to 10^6 efficiently. The input `n` is a positive integer, and the output should be a list of prime numbers less than `n`.
"""

import math

def generate_primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    prime = 2

    while prime <= math.sqrt(n):
        if is_prime[prime]:
            for i in range(prime * prime, n + 1, prime):
                is_prime[i] = False
        prime += 1

    primes = [i for i in range(2, n) if is_prime[i]]
    return primes