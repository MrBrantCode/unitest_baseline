"""
QUESTION:
Write a function `segmented_sieve` that finds all prime numbers within a given range `[start, end]` and returns them in a sorted order. The function should optimize for efficiency and minimize memory usage to handle larger ranges.
"""

import math

def segmented_sieve(start, end):
    limit = int(math.sqrt(end)) + 1
    primes = []

    # Create a boolean array "mark[0..limit]" and initialize all entries it as true.
    mark = [True] * limit

    for p in range(2, limit):
        # If p is not changed, then it is a prime
        if mark[p]:
            primes.append(p)
            # Update all multiples of p
            for i in range(p * p, limit, p):
                mark[i] = False

    result = []
    for num in range(start, end + 1):
        if all(num % p != 0 for p in primes):
            result.append(num)

    return result