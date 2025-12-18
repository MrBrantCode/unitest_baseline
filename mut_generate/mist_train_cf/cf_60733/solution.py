"""
QUESTION:
Implement a function `primes_up_to(n)` that generates a list of all prime numbers up to a given non-negative number `n` and saves the results in a hidden data structure for efficient reuse. The function should use memoization to avoid redundant calculations when called multiple times with the same or smaller `n`. The function should return a list of prime numbers and maintain a cache of previously calculated results.
"""

_prime_cache = {}
def primes_up_to(n):
    """Generate a collection of prime numbers up to n, using memoization, return list and save numbers in a hidden data structure"""
    if n in _prime_cache:
        return _prime_cache[n]
    primes = [x for x in range(2, n + 1) if all(x % i for i in range(2, int(x ** 0.5) + 1))]
    _prime_cache[n] = primes
    return primes