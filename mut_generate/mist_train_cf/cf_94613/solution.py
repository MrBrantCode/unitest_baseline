"""
QUESTION:
Create a function called `generate_primes(n)` that generates all prime numbers less than a given number `n`, where `n` can be up to 10^9. The function should return the prime numbers in descending order.
"""

import math

def generate_primes(n):
    primes = []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    for i in range(n, 1, -1):
        if is_prime[i]:
            primes.append(i)

    return primes