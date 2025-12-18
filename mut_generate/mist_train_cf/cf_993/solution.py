"""
QUESTION:
Create a function `primes_in_range` that takes two integers, `start` and `end`, and returns a list of all prime numbers between `start` and `end` (inclusive). The function should have a time complexity of O((end-start+1)*log(log(end))).
"""

import math

def primes_in_range(start, end):
    primes = []
    limit = math.isqrt(end) + 1
    sieve = [True] * (limit + 1)
    for p in range(2, limit + 1):
        if sieve[p]:
            for i in range(p * p, limit + 1, p):
                sieve[i] = False
            for i in range(max(p * p, (start // p) * p), end + 1, p):
                if i >= start:
                    if all(i % j != 0 for j in range(2, int(math.sqrt(i)) + 1)):
                        primes.append(i)
    for num in range(max(limit, start), end + 1):
        if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
            primes.append(num)
    return primes