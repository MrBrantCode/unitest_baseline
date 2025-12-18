"""
QUESTION:
Create a recursive function `generate_primes(n, p=2, primes=None)` that generates all prime numbers up to a given limit `n`. The function should use the Sieve of Eratosthenes algorithm and return a list of prime numbers. Note that `p` and `primes` are optional parameters with default values of `2` and `None`, respectively.
"""

def generate_primes(n, p=2, primes=None):
    if primes is None:
        primes = [True for _ in range(n)]
    if p*p > n:
        return [i for i in range(2, n) if primes[i]]
    if primes[p]:
        for i in range(p*p, n, p):
            primes[i] = False
    return generate_primes(n, p+1, primes)