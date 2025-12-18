"""
QUESTION:
Write a function called `sum_of_squares_of_primes` that calculates the sum of the squares of prime numbers within a given range, excluding 2 and 3. The prime numbers should be multiplied by 3 before adding to the sum. The function should take two parameters: `range_start` and `range_end`, representing the start and end of the range (inclusive).
"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_squares_of_primes(range_start, range_end):
    total = 0
    for num in range(range_start, range_end + 1):
        if num != 2 and num != 3 and is_prime(num):
            total += (num * 3) ** 2
    return total