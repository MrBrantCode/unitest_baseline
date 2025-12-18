"""
QUESTION:
Implement two functions: `is_prime(n)` and `generate_prime_numbers(n)`. The `is_prime(n)` function checks whether a given number `n` is prime or not and should have a time complexity of O(√n). The `generate_prime_numbers(n)` function generates all prime numbers up to a given number `n` and should have a time complexity of O(n log(log n)).
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def generate_prime_numbers(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes