"""
QUESTION:
Implement a function called `sieve_of_eratosthenes` that uses the Sieve of Eratosthenes algorithm to generate all prime numbers up to a given number `n`. The function should return a list of prime numbers. The input `n` will be a positive integer, and the output list should contain all prime numbers from 2 to `n`. The function should have a time complexity of O(n log log n) and a space complexity of O(n).
"""

import math

def sieve_of_eratosthenes(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False

    for i in range(2, int(math.sqrt(n))+1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False

    return [num for num, is_prime in enumerate(primes) if is_prime]