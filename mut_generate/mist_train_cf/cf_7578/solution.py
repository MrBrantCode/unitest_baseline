"""
QUESTION:
Write a program with functions `sieve_of_eratosthenes`, `calculate_sum_of_primes`, `calculate_product_of_primes`, and `find_primes_in_range` that take an integer `n` and/or a range as input and return the following: 

- `sieve_of_eratosthenes`: a list of all prime numbers up to `n` using the Sieve of Eratosthenes algorithm with a time complexity of O(n*log(log(n))).
- `calculate_sum_of_primes`: the sum of all prime numbers up to `n`.
- `calculate_product_of_primes`: the product of all prime numbers up to `n`.
- `find_primes_in_range`: a list of all prime numbers within a given range.

The functions should handle large input values efficiently without exceeding the specified time complexity.
"""

import math

def sieve_of_eratosthenes(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False

    for p in range(2, int(math.sqrt(n))+1):
        if primes[p]:
            for i in range(p*p, n+1, p):
                primes[i] = False

    return [i for i, is_prime in enumerate(primes) if is_prime]

def calculate_sum_of_primes(n):
    primes = sieve_of_eratosthenes(n)
    return sum(primes)

def calculate_product_of_primes(n):
    primes = sieve_of_eratosthenes(n)
    product = 1
    for prime in primes:
        product *= prime
    return product

def find_primes_in_range(start, end):
    primes = sieve_of_eratosthenes(end)
    return [prime for prime in primes if prime >= start]