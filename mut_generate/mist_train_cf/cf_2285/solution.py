"""
QUESTION:
Create a function `generate_primes(n)` that generates the first n prime numbers using the segmented sieve algorithm, where n is a positive integer greater than 1 and less than or equal to 10^6.
"""

import math

def generate_primes(n):
    if n <= 1:
        return []

    primes = [2]
    i = 3

    while len(primes) < n:
        is_prime = True

        if i % 2 == 0:
            i += 1
            continue

        for prime in primes:
            if i % prime == 0:
                is_prime = False
                break
            if prime * prime > i:
                break

        if is_prime:
            primes.append(i)

        i += 2

    return primes[:n]