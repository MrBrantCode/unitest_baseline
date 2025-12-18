"""
QUESTION:
Create a function called `generate_primes` that takes an integer `n` as input and returns a list of all prime numbers less than `n`. The function should be able to handle inputs up to 10^6 efficiently.
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

    primes = [i for i in range(2, n + 1) if is_prime[i]]
    return primes