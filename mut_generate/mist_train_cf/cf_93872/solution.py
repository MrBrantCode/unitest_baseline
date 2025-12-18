"""
QUESTION:
Create a function called `print_prime_numbers` that prints all prime numbers from a given number down to 2. The function should have a time complexity of O(sqrt(n)) where n is the given number, and should not use any loops or conditional statements (but may use recursive functions that use conditional statements internally). The function should take one argument: a positive integer n.
"""

import math

def print_prime_numbers(n, i=2):
    if n < 2:
        return
    if is_prime(n):
        print(n)
    print_prime_numbers(n - 1)

def is_prime(n, i=2):
    if n < 2:
        return False
    if i > math.isqrt(n):
        return True
    if n % i == 0:
        return False
    return is_prime(n, i + 1)