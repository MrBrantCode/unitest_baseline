"""
QUESTION:
Implement a function called `sieve_of_eratosthenes` that generates all prime numbers up to the provided number `n` using the Sieve of Eratosthenes algorithm. The function should return a list of prime numbers. If `n` is less than 2, the function should return an error message. The function should be optimized for time complexity of O(n log(log n)) and be able to handle very large numbers efficiently without causing memory overflow.
"""

import math

def sieve_of_eratosthenes(n):
    if n < 2:
        return "Error: Number must be greater than or equal to 2"
    
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(math.sqrt(n))+1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    
    return [i for i in range(2, n+1) if sieve[i]]