"""
QUESTION:
Create a function named `is_prime_palindrome` that takes a single integer `n` as input. The function should return `True` if `n` is both a prime number and a palindrome, and `False` otherwise. The function should only consider positive integers, and the input `n` is guaranteed to be an integer.
"""

import math

def is_prime(n):
    # Helper function to check if a number is prime
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_prime_palindrome(n):
    # Check if the number is a positive integer
    if not isinstance(n, int) or n <= 0:
        return False

    # Check if the number is prime
    if not is_prime(n):
        return False

    # Check if the number is a palindrome
    if str(n) != str(n)[::-1]:
        return False

    # Both conditions are satisfied
    return True