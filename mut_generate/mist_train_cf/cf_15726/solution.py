"""
QUESTION:
Create a function named `print_prime_numbers` that prints all prime numbers from the given input number down to 2 without using loops or conditional statements. The time complexity should be O(sqrt(n)), where n is the given number.
"""

import math

def print_prime_numbers(n, i=2):
    if n < 2:
        return
    if is_prime(n, i):
        print(n)
    print_prime_numbers(n - 1, i)

def is_prime(n, i=2):
    if i > math.isqrt(n):
        return True
    if n % i == 0:
        return False
    return is_prime(n, i + 1)