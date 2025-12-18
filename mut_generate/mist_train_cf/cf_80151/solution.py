"""
QUESTION:
Write a function named `prime_intersection` that takes four positive integers as input: `start_1`, `end_1`, `start_2`, and `end_2`, representing two ranges [start_1, end_1] and [start_2, end_2]. The function should return a list of prime numbers that lie within the intersection of the two ranges. The ranges can overlap partially or completely, and each interval is at least 100 numbers apart. Ensure the solution is efficient for larger ranges.
"""

def prime_intersection(start_1, end_1, start_2, end_2):
    def sieve_eratosthenes(n):
        primes = [True] * (n + 1)
        p = 2
        while p * p <= n:
            if primes[p] is True:
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1
        primes[0] = False
        primes[1] = False
        return [p for p, is_prime in enumerate(primes) if is_prime]

    max_limit = max(end_1, end_2)
    primes = sieve_eratosthenes(max_limit)
    return [prime for prime in primes if max(start_1, start_2) <= prime <= min(end_1, end_2)]