"""
QUESTION:
Write a function named `is_prime` that takes a number as input and returns `True` if it is a prime number, and `False` otherwise. The function should be used in conjunction with the built-in `filter` function to filter a list of numbers and return a new list containing only the prime numbers. The input list is not specified, so the function should work with any list of integers.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True