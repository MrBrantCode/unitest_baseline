"""
QUESTION:
Write a function named `prime_factors(n)` that takes an integer `n` as input and returns a list of its prime factors in descending order. The function should be able to handle input numbers up to 10^12.
"""

import math

def prime_factors(n):
    primes = []

    while n % 2 == 0:
        primes.append(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            primes.append(int(i))
            n = n / i

    if n > 2:
        primes.append(int(n))

    return sorted(primes, reverse=True)