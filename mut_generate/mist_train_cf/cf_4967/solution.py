"""
QUESTION:
Create a function named `is_prime`, `is_perfect_square`, and `is_palindrome` to check whether a given positive integer is a prime number, a perfect square, and a palindrome respectively. Each function should take a positive integer as input and return a boolean indicating whether the number meets the corresponding condition.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect_square(n):
    square_root = math.isqrt(n)
    return square_root * square_root == n

def is_palindrome(n):
    number_str = str(n)
    return number_str == number_str[::-1]