"""
QUESTION:
Write a function named `is_prime_and_divisible_by_five` that takes a list of integers as input, iterates through the list, and prints out the numbers that are both prime and divisible by 5. A prime number is a positive integer greater than 1 that has no positive divisors other than 1 and itself. Note that the list may contain negative numbers, but prime numbers are defined only for positive integers. The function should not use any built-in Python functions for checking primality or divisibility.
"""

def is_prime_and_divisible_by_five(num):
    if num < 2 or num % 5 != 0:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True