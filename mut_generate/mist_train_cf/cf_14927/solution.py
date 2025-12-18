"""
QUESTION:
Create a function `count_primes_in_range` that takes an integer `n` as input and returns the count of prime numbers from 2 to `n` (inclusive). The function should use an efficient algorithm with a time complexity of O(n log log n) and a space complexity of O(n).
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

    # add count of remaining primes
    for k in range(int(math.sqrt(n)) + 1, n + 1):
        if isPrime[k]:
            count += 1

    return count