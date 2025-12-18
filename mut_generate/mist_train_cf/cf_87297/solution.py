"""
QUESTION:
Implement a function `unique_prime_numbers` that takes a list of numbers as input, where the numbers can be integers or floats, and returns a set containing the unique prime numbers from the list. Exclude any negative numbers from the input list and handle floating-point numbers by rounding them to the nearest integer. If the input list is empty or contains no prime numbers, return an empty set.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def unique_prime_numbers(numbers):
    primes = set()
    for num in numbers:
        if isinstance(num, float):
            num = round(num)
        if isinstance(num, int) and num > 0 and is_prime(num):
            primes.add(num)
    return primes