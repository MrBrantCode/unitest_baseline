"""
QUESTION:
Write a Python function `generate_prime_list` that takes two integers `start` and `end` as input, generates a list of prime numbers between `start` and `end` (inclusive), and returns the list along with the sum of all prime numbers in the list. Assume that `start` and `end` are positive integers and `start` is less than or equal to `end`.
"""

import math

def generate_prime_list(start, end):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    prime_list = [num for num in range(start, end+1) if is_prime(num)]
    return prime_list, sum(prime_list)