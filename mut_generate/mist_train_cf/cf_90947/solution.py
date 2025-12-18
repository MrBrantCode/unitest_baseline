"""
QUESTION:
Create a function called `generate_prime_numbers` that takes two parameters, `start` and `end`, representing the start and end of a range. The function should return a list of all prime numbers within the range `[start, end]` (inclusive) with a time complexity of O(n√m) and a space complexity of O(n), where n is the length of the range and m is the maximum value in the range.
"""

import math

def generate_prime_numbers(start, end):
    primes = []
    for num in range(start, end+1):
        if is_prime(num):
            primes.append(num)
    return primes

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True