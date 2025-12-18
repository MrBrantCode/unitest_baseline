"""
QUESTION:
Write a function `f(n)` that returns the natural logarithm of the smallest positive integer which does not share a coprime relationship with any positive integer `m <= n` that has 3 as its least significant digit. The result should be rounded to six decimal places.
"""

import math

def entrance(n):
    sieve = [True] * (n+1)
    for x in range(2, int(n**0.5) + 1):
        if sieve[x]: 
            for u in range(2*x, n+1, x):
                sieve[u] = False
    primes = [num for num in range(3, n+1) if sieve[num] and num%10==3]
    result = 1
    for p in primes:
        result *= p
    return round(math.log(result), 6)