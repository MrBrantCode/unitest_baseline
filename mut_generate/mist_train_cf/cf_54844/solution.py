"""
QUESTION:
Write a function `least_common_multiple` that calculates the least common multiple of all prime numbers up to a given limit, excluding twin primes. The function should take an integer `limit` as input and return the LCM of the non-twin prime numbers up to that limit. The input `limit` is a positive integer greater than 1.
"""

import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_twin_prime(n):
    return is_prime(n) and is_prime(n + 2)

def least_common_multiple(limit):
    lcm = 1
    for i in range(2, limit + 1):
        if is_prime(i) and not is_twin_prime(i):
            lcm *= i
    return lcm