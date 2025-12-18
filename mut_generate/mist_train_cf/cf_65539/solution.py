"""
QUESTION:
Write a function named `nthSuperUglyNumber` that takes two inputs: a positive integer `n` and a sorted array of unique prime numbers `primes`, and returns the `n`-th super ugly number, which is a positive integer whose prime factors are all contained within the array `primes`. The constraints are: `1 <= n <= 10^6`, `1 <= len(primes) <= 100`, and `2 <= primes[i] <= 1000`.
"""

import heapq

def nthSuperUglyNumber(n, primes):
    uglies = [1]
    def gen(prime):
        for ugly in uglies:
            yield ugly * prime
    merged = heapq.merge(*map(gen, primes))
    while len(uglies) < n:
        ugly = next(merged)
        if ugly != uglies[-1]:
            uglies.append(ugly)
    return uglies[-1]