"""
QUESTION:
Create a function called `prime_pairs` that takes a list of integers as input and returns a list of tuples. Each tuple should contain two distinct prime numbers from the input list in ascending order. The function should be efficient in terms of time and memory complexity and the resulting list of tuples should be in ascending order.
"""

import itertools

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_pairs(numbers):
    primes = [num for num in numbers if is_prime(num)]
    return sorted([tuple(sorted(pair)) for pair in itertools.combinations(primes, 2)])