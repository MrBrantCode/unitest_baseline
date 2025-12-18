"""
QUESTION:
Implement a function `count_primes_and_twin_primes(n)` that takes an integer `n` as input and returns a tuple containing two values: the count of prime numbers less than or equal to `n` and the count of twin prime pairs within the same range. A twin prime pair is a pair of prime numbers that differ by 2. The function should use the Sieve of Eratosthenes algorithm to efficiently find prime numbers and should handle edge cases where `n` is less than or equal to 2, or not an integer. Additionally, the function should utilize a caching mechanism to prevent recalculation for repeated input values.
"""

from functools import lru_cache

def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while p ** 2 <= n:
        if prime[p] == True:
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1

    return [p for p in range(2, n + 1) if prime[p]]

@lru_cache(maxsize = 1000)
def count_primes_and_twin_primes(n):
    if not isinstance(n, int) or n < 2:
        print("The input has to be an integer greater than 2.")
        return None

    primes = SieveOfEratosthenes(n)
    twin_primes = [(primes[i], primes[i + 1]) for i in range(len(primes) - 1) if primes[i + 1] - primes[i] == 2]

    return len(primes), len(twin_primes)