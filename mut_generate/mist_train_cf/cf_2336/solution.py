"""
QUESTION:
Create a function called `generate_primes` that takes an integer `limit` as input and returns a list of all prime numbers less than `limit` in descending order. The function should be able to handle inputs up to 10^9 efficiently.
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