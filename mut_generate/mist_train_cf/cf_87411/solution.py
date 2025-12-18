"""
QUESTION:
Create a function named `generate_primes(limit)` that generates all prime numbers less than a given number `limit` and returns them in descending order. The function should be efficient enough to handle inputs up to 10^9.
"""

import math

def generate_primes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for number in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[number]:
            for multiple in range(number * number, limit + 1, number):
                is_prime[multiple] = False

    primes = [index for index, value in enumerate(is_prime) if value]
    primes.reverse()

    return primes