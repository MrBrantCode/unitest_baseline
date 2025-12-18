"""
QUESTION:
Write a function named `generate_primes` that generates the first `n` prime numbers. The function should start from 2 and identify prime numbers in increasing order. The function should return a list of the first `n` prime numbers.
"""

def generate_primes(n):
    primes = []
    candidate = 2
    while len(primes) < n:
        if all(candidate % prime != 0 for prime in primes):
            primes.append(candidate)
        candidate += 1
    return primes