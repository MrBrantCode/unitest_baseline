"""
QUESTION:
Generate an array of length n containing the square of prime numbers from 1 to n, excluding any number that is divisible by 3. The function name should be generate_square_primes(n).
"""

import math

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    
    prime_numbers = []
    for i in range(2, n + 1):
        if primes[i]:
            prime_numbers.append(i)
    
    return prime_numbers

def generate_square_primes(n):
    prime_numbers = sieve_of_eratosthenes(n)
    
    square_primes = []
    for prime in prime_numbers:
        if prime % 3 != 0:
            square_primes.append(prime ** 2)
    
    return square_primes