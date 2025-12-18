"""
QUESTION:
Create a function called `prime_palindrome` that takes an integer `n` between 1 and 10^12 as input and returns a boolean value indicating whether the number is both a palindrome and a prime number. The function should be efficient for large numbers.
"""

import math

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    n_str = str(n)
    return n_str == n_str[::-1]

def prime_palindrome(n):
    return is_palindrome(n) and is_prime(n)