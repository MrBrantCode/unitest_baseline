"""
QUESTION:
Create a function called `prime_numbers(n)` that generates a sequence of prime numbers ranging from 2 up to a given limit `n`. The function should be efficient enough to support a limit of 1,000,000 or higher. It should return a list of prime numbers. The function should have a time complexity of O(n log(log n)) and space complexity of O(n).
"""

import math

def prime_numbers(n):
    """ Generate prime numbers up to n """
    sieve = [True] * (n+1)
    for x in range(2, int(math.sqrt(n)) + 1):
        if sieve[x]: 
            # mark multiples of x as not prime
            for i in range(x*x, n+1, x):
                sieve[i] = False
    
    # collect all prime numbers
    primes = [p for p in range(2, n+1) if sieve[p]]
    return primes