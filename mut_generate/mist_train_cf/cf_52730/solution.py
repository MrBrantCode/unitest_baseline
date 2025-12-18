"""
QUESTION:
Create a function named `cumulative_sum_of_squares_of_primes(n)` that calculates the cumulative sum of the squares of all prime numbers from 1 to n (inclusive). Implement a less common, efficient algorithm to determine if a number is prime.
"""

import numpy as np

def cumulative_sum_of_squares_of_primes(n):
    primes = np.full((n+1,), True, dtype=bool)
    primes[0:2] = False
    for ind, val in enumerate(primes):
        if val is True:
            primes[ind ** 2::ind] = False
    return sum([i ** 2 for i, val in enumerate(primes) if val is True])