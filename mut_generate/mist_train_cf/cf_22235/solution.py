"""
QUESTION:
Write a function named `is_prime` that checks if a given number is prime. The function should return True if the number is prime and False otherwise. Additionally, write a function named `get_primes_in_range` that takes two parameters, `lower_limit` and `upper_limit`, and returns a list of all prime numbers within the specified range (inclusive). The `get_primes_in_range` function should execute in O(n) time complexity, where n is the difference between `upper_limit` and `lower_limit`.
"""

import math

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def get_primes_in_range(lower_limit, upper_limit):
    primes_in_range = []
    for num in range(lower_limit, upper_limit + 1):
        if is_prime(num):
            primes_in_range.append(num)
    return primes_in_range