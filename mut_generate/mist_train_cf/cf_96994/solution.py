"""
QUESTION:
Write a function named `sum_of_primes_in_range` that calculates and returns the sum of all prime numbers between two given numbers, `start` (inclusive) and `end` (inclusive), where `start` and `end` are integers and `start` is less than or equal to `end`.
"""

import math

def sum_of_primes_in_range(start, end):
    total_sum = 0
    for num in range(start, end + 1):
        if is_prime(num):
            total_sum += num
    return total_sum

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True