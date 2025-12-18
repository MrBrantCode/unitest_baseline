"""
QUESTION:
Implement a function `is_prime` to check if a given non-negative integer `n` is prime and a function `primes_up_to` to generate a list of all prime numbers up to a specified non-negative number `n`. 

In the `primes_up_to` function, utilize a hidden data structure to store prime numbers for better efficiency in repetitive calls with the same or smaller numbers.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):    
        if n % i == 0:
            return False
    return True

def primes_up_to(n):
    if not hasattr(primes_up_to, 'primes') or n > primes_up_to.max_checked:
        primes_up_to.primes = [True] * (n + 1)
        primes_up_to.primes[0:2] = [False, False]  
        primes_up_to.max_checked = n
        p = 2
        while (p * p <= n):
            if (primes_up_to.primes[p] == True):
                for i in range(p * p, n+1, p):
                    primes_up_to.primes[i] = False
            p += 1
    return [x for x in range(2, n + 1) if primes_up_to.primes[x]]

primes_up_to.primes = None
primes_up_to.max_checked = -1