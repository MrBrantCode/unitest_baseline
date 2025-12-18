"""
QUESTION:
Write a function named `count_primes_in_range` that takes an integer `n` as input, representing the upper limit of a range, and returns the total count of prime numbers within the range from 2 to `n`. The function should optimize for time complexity and be mindful of memory constraints.
"""

import math

def count_primes_in_range(n):
    isPrime = [True] * (n + 1)
    isPrime[0] = isPrime[1] = False
    count = 0

    for i in range(2, int(math.sqrt(n)) + 1):
        if isPrime[i]:
            count += 1
            for j in range(i * i, n + 1, i):
                isPrime[j] = False

    for i in range(int(math.sqrt(n)) + 1, n + 1):
        if isPrime[i]:
            count += 1

    return count