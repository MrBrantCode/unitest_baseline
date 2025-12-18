"""
QUESTION:
Create a function named `is_prime_palindrome(n)` that checks if a given number `n` is a prime palindrome number, which is a number that is both prime and a palindrome. The function should return `True` if `n` is a prime palindrome number and `False` otherwise. The input `n` should be a positive integer.
"""

import math

def is_prime_palindrome(n):
    # Check if the number is a positive integer
    if not isinstance(n, int) or n <= 0:
        return False

    # Helper function to check if a number is prime
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    # Check if the number is prime and a palindrome
    return is_prime(n) and str(n) == str(n)[::-1]