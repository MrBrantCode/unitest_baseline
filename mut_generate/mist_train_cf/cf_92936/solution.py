"""
QUESTION:
Implement a function named `sieve_of_eratosthenes` that generates prime numbers up to a given number `n` using the Sieve of Eratosthenes algorithm with the following conditions:

- The function should handle the case when the provided number `n` is less than 2 and return an error message.
- The function should return a list of prime numbers instead of printing them.
- The function should have a time complexity of O(n log(log n)) and handle large numbers efficiently without causing memory overflow.
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