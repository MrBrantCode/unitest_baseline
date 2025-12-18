"""
QUESTION:
Write a function named `sum_of_primes` that calculates and returns the sum of all prime numbers between two given numbers, `start` and `end` (inclusive). The function should not take any arguments other than `start` and `end`, and it should not print any output. The input range is guaranteed to be valid (i.e., `start` and `end` are integers, and `start` is less than or equal to `end`).
"""

import math

def sum_of_primes(start, end):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    total_sum = 0
    for num in range(start, end + 1):
        if is_prime(num):
            total_sum += num
    return total_sum