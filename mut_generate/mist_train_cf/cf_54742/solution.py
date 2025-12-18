"""
QUESTION:
Create a function called `twin_primes` that generates all twin primes (pairs of primes that differ by two) up to a given limit `n`. The function should return a list of tuples, where each tuple represents a pair of twin primes. The function should be optimized for high input values (beyond 1,000,000) and should minimize computation time.
"""

import numpy as np

def twin_primes(n):
    sieve = np.ones(n//3 + (n%6==2), dtype=bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False

    primes = np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]
    return [(primes[i], primes[i+1]) for i in range(len(primes)-1) if primes[i+1]-primes[i] == 2]