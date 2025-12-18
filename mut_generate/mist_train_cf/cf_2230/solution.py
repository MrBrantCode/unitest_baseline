"""
QUESTION:
Write a function named is_prime that takes an integer parameter num and returns True if num is a prime number, otherwise False. 

The is_prime function should not use any built-in functions for prime number generation. It should return False if num is less than 2, otherwise, it should iterate from 2 to the square root of num (inclusive) and return False if num is divisible by any of the iterated numbers. If the loop completes without finding a divisor, return True.

Use the is_prime function to generate the first 100 prime numbers.
"""

import math

def is_prime(num):
    """
    Checks if a number is prime.

    Args:
    num (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True