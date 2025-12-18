"""
QUESTION:
Write a function named `lcm_of_primes` that calculates the least common multiple (LCM) of all prime numbers within a specified range, from `start` (inclusive) to `end` (inclusive), with a time complexity of O(n log log n).
"""

from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def primes_sieve(limit):
    limit += 1
    a = [True] * limit
    a[0] = a[1] = False

    for i,isprime in enumerate(a):
        if isprime:
            for n in range(i * i, limit, i):
                a[n] = False

    return [i for i, isprime in enumerate(a) if isprime]

def lcm_of_primes(start, end):
    primes = primes_sieve(end)
    primes = [prime for prime in primes if prime >= start]
    
    result = 1
    for prime in primes:
        result = lcm(result, prime)

    return result