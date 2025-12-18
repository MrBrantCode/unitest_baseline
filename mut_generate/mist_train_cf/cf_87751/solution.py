"""
QUESTION:
Generate an array of length n that contains the square of the prime numbers from 1 to n, but excluding any number that is divisible by 3. Implement the function `generate_square_primes(n)` that uses the Sieve of Eratosthenes algorithm to find the prime numbers.
"""

import math

def generate_square_primes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
                
    square_primes = []
    for i in range(2, n + 1):
        if primes[i] and i % 3 != 0:
            square_primes.append(i ** 2)
    
    return square_primes