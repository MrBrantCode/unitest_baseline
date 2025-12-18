"""
QUESTION:
Write a function named `is_prime` that takes an integer `num` as input and returns `True` if it is a prime number and `False` otherwise. Use this function to print all prime numbers within a given range in ascending order. The function should handle any given range defined by two integers `lower_range` and `upper_range`. The function should not take any parameters other than the number to check for primality.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True