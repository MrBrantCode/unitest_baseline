"""
QUESTION:
Create a function `list_prime_numbers(start, end)` that takes two parameters `start` and `end` and returns a list of prime numbers between `start` and `end` (inclusive), while also displaying a warning message if either `start` or `end` is negative, or if `start` is greater than `end`. The function should check for primality by testing divisibility up to the square root of each number.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def list_prime_numbers(start, end):
    if start < 0 or end < 0:
        print("Warning: Both numbers must be non-negative.")
        return []
    if start > end:
        print("Warning: The first number must be smaller than the second number.")
        return []

    prime_numbers = []
    for num in range(start, end + 1):
        if is_prime(num):
            prime_numbers.append(num)

    return prime_numbers