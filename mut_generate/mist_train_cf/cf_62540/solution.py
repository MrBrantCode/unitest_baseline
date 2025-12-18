"""
QUESTION:
Create a function `smallest_evenly_divisible` that returns the smallest positive number that is evenly divisible by all of the prime numbers from 1 to a given limit (in this case, 100). The function should be optimized to run efficiently for large inputs and should only use the prime numbers within the given limit.
"""

import math

def smallest_evenly_divisible(n):
    primes = []
    sieve = [True] * (n+1)
    for x in range(2, int(n**0.5) + 1):
        if sieve[x]: 
            for i in range(x*x, n+1, x): 
                sieve[i] = False
    for x in range(2, n):
        if sieve[x]: 
            primes.append(x)
    lcm = 1
    for i in primes:
        lcm = lcm * i // math.gcd(lcm, i)
    return lcm