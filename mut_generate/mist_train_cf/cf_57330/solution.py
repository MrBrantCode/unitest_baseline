"""
QUESTION:
Implement a function named `prime_numbers(n, m)` that generates prime numbers up to `n` using the Sieve of Eratosthenes algorithm and returns the `m`-th prime number in the sequence. The function should take two parameters: `n`, the upper limit for the range within which to identify prime numbers, and `m`, the position of the prime number to be returned. The function should return the `m`-th prime number in the sequence.
"""

def prime_numbers(n, m):
    sieve = [True] * (n+1)
    p = 2
    while p * p <= n:
        if sieve[p] is True:
            for i in range(p * p, n+1, p):
                sieve[i] = False
        p += 1

    primes = [p for p in range(2, n+1) if sieve[p]]
    return primes[m-1]