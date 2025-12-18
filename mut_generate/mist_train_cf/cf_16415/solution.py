"""
QUESTION:
Define a function `findPrimesInRange(start, end)` that takes the starting and ending numbers of a range as input. The function should return a list of all prime numbers within the given range in ascending order. The function should have a time complexity of O(n log log n), where n is the given range.
"""

import math

def findPrimesInRange(start, end):
    isPrime = [True] * (end + 1)
    for i in range(2, int(math.sqrt(end)) + 1):
        if isPrime[i]:
            for j in range(i * i, end + 1, i):
                isPrime[j] = False

    primes = []
    for i in range(start, end + 1):
        if isPrime[i]:
            primes.append(i)

    return primes