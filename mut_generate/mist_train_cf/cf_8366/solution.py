"""
QUESTION:
Create a function `segmented_sieve` that takes two parameters, `lower` and `upper`, representing the lower and upper bounds of a range of integers. The function should return a list of all prime numbers between `lower` and `upper` (inclusive), where the difference between `lower` and `upper` is at most 10^18. The function should be efficient and scalable to handle large ranges.
"""

import math

def segmented_sieve(lower, upper):
    limit = int(math.sqrt(upper)) + 1
    is_prime = [True] * limit

    for i in range(2, limit):
        if is_prime[i]:
            for j in range(i * i, limit, i):
                is_prime[j] = False

    primes = []
    for i in range(2, limit):
        if is_prime[i]:
            primes.append(i)

    segmented_primes = []
    for low in range(lower, upper + 1, limit):
        high = min(low + limit - 1, upper)
        is_segment_prime = [True] * (high - low + 1)

        for prime in primes:
            start = math.ceil(low / prime) * prime
            if start == prime:
                start = prime * prime

            for j in range(start, high + 1, prime):
                is_segment_prime[j - low] = False

        for i in range(low, high + 1):
            if is_segment_prime[i - low] and i > 1:
                segmented_primes.append(i)

    return segmented_primes