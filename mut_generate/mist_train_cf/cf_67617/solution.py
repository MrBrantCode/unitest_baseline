"""
QUESTION:
Write a Python function named `prod_primes` that takes two integers `min_val` and `max_val` as input and returns the product of all prime numbers within the specified range `[min_val, max_val]`. 

The function should include exception handling mechanisms to raise an exception if `min_val` is less than 2 or `min_val` is greater than `max_val`. 

Additionally, the prime finding functionality should be implemented as a separate function `find_primes` that uses recursion to find prime numbers up to a given number `n`. The calculation of the product of prime numbers should also be implemented as a separate functionality within `prod_primes`.
"""

import math

def find_primes(n, primes = [2]):
    if primes[-1] >= n:
        return [x for x in primes if x <= n]
    else:
        for i in range(primes[-1]+1, n+1):
            is_prime = True
            for j in range(2, int(math.sqrt(i))+1):
                if (i % j) == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(i)
        return primes

def prod_primes(min_val, max_val):
    if min_val > max_val: 
        raise Exception("Invalid range: minimum range value is greater than maximum range value")
    if min_val < 2: 
        raise Exception("Invalid range: minimum range value is less than 2")
    primes = find_primes(max_val)
    primes = [x for x in primes if x >= min_val]
    prod_out = 1
    for x in primes:
        prod_out *= x
    return prod_out