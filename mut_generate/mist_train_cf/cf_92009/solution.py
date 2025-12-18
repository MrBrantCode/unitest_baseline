"""
QUESTION:
Create a script with two functions: `is_prime(num)` that checks whether a given number is a prime number and returns a boolean value, and `print_prime_numbers(n)` that prints all prime numbers up to a given integer `n`. The `is_prime(num)` function should only take an integer as input and return `True` if the number is prime and `False` otherwise. The `print_prime_numbers(n)` function should only take an integer `n` as input and print all prime numbers up to `n`.
"""

import math

def is_prime(num):
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