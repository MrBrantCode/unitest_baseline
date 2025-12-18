"""
QUESTION:
Create a function named `generate_primes(n)` that takes an integer `n` as input and returns a list of all prime numbers from 2 to `n`.
"""

def generate_primes(n):
    sieve = [True] * (n+1)
    for x in range(2, int(n**0.5) + 1):
        if sieve[x]:
            for i in range(x*x, n+1, x):
                sieve[i] = False
    return [p for p in range(2, n+1) if sieve[p]]