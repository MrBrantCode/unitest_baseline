"""
QUESTION:
Write a function `generate_smooth_numbers(primes, limit)` that generates all numbers up to `limit` that are products of prime numbers in the `primes` list raised to any power.
"""

import itertools

def generate_smooth_numbers(primes, limit):
    def helper(t, i):
        if i == len(primes):
            yield t
        else:
            p = primes[i]
            for _ in itertools.count():
                if t > limit:
                    break
                yield from helper(t, i + 1)
                t *= p

    return sorted(helper(1, 0))