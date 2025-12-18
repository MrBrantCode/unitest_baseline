"""
QUESTION:
# Summation Of Primes

The sum of the primes below or equal to 10 is **2 + 3 + 5 + 7 = 17**. Find the sum of all the primes **_below or equal to the number passed in_**.

From Project Euler's [Problem #10](https://projecteuler.net/problem=10 "Project Euler - Problem 10").
"""

from bisect import bisect

def sieve(n):
    (sieve, primes) = ([0] * (n + 1), [])
    for i in range(2, n + 1):
        if not sieve[i]:
            primes.append(i)
            for j in range(i ** 2, n + 1, i):
                sieve[j] = 1
    return primes

PRIMES = sieve(1000000)

def sum_of_primes_below(n):
    return sum(PRIMES[:bisect(PRIMES, n)])