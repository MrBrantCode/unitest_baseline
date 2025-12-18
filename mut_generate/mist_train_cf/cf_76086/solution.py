"""
QUESTION:
Create a function called `primesLessThan` that takes an integer `n` as input and returns a list of all prime numbers less than `n`. The function should return an empty list if `n` is less than 2.
"""

import math
def primesLessThan(n):
    if n < 2:
        return []
    
    primes = []
    
    for possible_prime in range(2, n):
        is_prime = True
        for num in range(2, math.isqrt(possible_prime)+1):
            if possible_prime % num == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(possible_prime)
    
    return primes