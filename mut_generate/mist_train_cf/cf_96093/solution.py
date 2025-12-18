"""
QUESTION:
Find all prime numbers less than a specified number 'n' using the Sieve of Eratosthenes algorithm and calculate their sum. 

The function should be named find_primes and take one argument: n, which is the upper limit for finding prime numbers. The function should return a list of prime numbers and their sum. 

The numbers should be in the range from 2 to n-1. The function should not take any other arguments.
"""

import math

def find_primes(n):
    primes = []
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False

    for p in range(2, int(math.sqrt(n))+1):
        if sieve[p]:
            for i in range(p*p, n+1, p):
                sieve[i] = False

    for p in range(2, n+1):
        if sieve[p]:
            primes.append(p)

    return primes, sum(primes)