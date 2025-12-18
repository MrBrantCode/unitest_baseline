"""
QUESTION:
Implement a function named `is_prime_palindrome(n)` that checks if a given positive integer `n` is both a prime number and a palindrome. The function should return a boolean value indicating whether `n` is a prime palindrome or not.
"""

import math

def is_prime_palindrome(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Convert number to string and check if it is a palindrome
    if str(n) != str(n)[::-1]:
        return False
    
    # Check if number is divisible by any values from 3 to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    
    return True