"""
QUESTION:
Write a function `generate_prime_numbers(start, end)` that generates a list of all prime numbers within a given range, inclusive. The function should use an efficient algorithm to determine whether a number is prime or not, and should handle large ranges efficiently.
"""

import math

def generate_prime_numbers(start, end):
    prime_numbers = []
    for num in range(start, end + 1):
        if num < 2:
            continue
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                break
        else:
            prime_numbers.append(num)
    return prime_numbers