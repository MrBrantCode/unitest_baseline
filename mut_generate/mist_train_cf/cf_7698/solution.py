"""
QUESTION:
Write a function `prime_numbers` that takes two integers `start` and `end` as parameters and returns a tuple containing a list of all prime numbers between `start` and `end` (inclusive), and the sum of these prime numbers.
"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers(start, end):
    prime_nums = [num for num in range(start, end+1) if is_prime(num)]
    return (prime_nums, sum(prime_nums))