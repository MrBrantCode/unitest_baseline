"""
QUESTION:
Create a function called `prime_generator` that generates an infinite series of prime numbers in ascending order. The function should be a generator that yields prime numbers on-the-fly, without storing them in memory, to ensure efficiency even for large prime numbers. The function should start from 2 and check each sequential number to determine if it is prime.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_generator():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1