"""
QUESTION:
Write a function `is_prime(n, m)` that returns a dictionary where the keys are integers from `n` to `m` (inclusive) and the values are boolean indicating whether the corresponding key is a prime number. Implement the Sieve of Eratosthenes technique to determine primality. If `n` is less than 2, start the sieve from 2.
"""

def is_prime(n, m):
    n = max(2, n)
    sieve = [True] * (m+1)
    sieve[0] = sieve[1] = False
    for x in range(4, m+1, 2):
        sieve[x] = False
    for x in range(3, int(m**0.5) + 1, 2):
        for y in range(x**2, m+1, x):
            sieve[y] = False
    return {x: sieve[x] for x in range(n, m+1)}