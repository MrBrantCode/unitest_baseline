"""
QUESTION:
Design a function `generate_primes(limit)` that generates and returns a list of all prime numbers from 2 up to the given `limit`.
"""

def generate_primes(limit):
    primes = []
    for n in range(2, limit + 1):
        if all(n % p > 0 for p in primes):
            primes.append(n)
    return primes