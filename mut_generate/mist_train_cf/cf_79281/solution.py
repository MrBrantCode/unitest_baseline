"""
QUESTION:
Create a function `check_prime(n)` that takes an integer `n` as input and returns `True` if it's a prime number, `False` otherwise. Then, use this function to iterate over an array of integers, check if each number is prime, and calculate the factorial of the prime numbers. Handle edge cases and errors. The function should not take any additional inputs besides `n`.
"""

import math

def check_prime(n):
    """
    Checks if a number is prime.

    Args:
    n (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if n <= 1:  # 1 and numbers below are not considered prime
        return False
    if n == 2 or n == 3:  # 2 and 3 are prime numbers
        return True
    if n % 2 == 0 or n % 3 == 0:  # if n is divisible by 2 or 3, it's not prime
        return False
    i = 5
    while i * i <= n:  # check divisibility upto the sqrt of n
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True