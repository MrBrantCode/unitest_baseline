"""
QUESTION:
Create a function named `is_prime(num)` that checks whether a given integer `num` is a prime number and returns a boolean value. Also, create a function named `print_prime_numbers(n)` that prints all prime numbers up to a given integer `n`.
"""

import math

def entrance(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def print_prime_numbers(n):
    for num in range(2, n+1):
        if entrance(num):
            print(num)