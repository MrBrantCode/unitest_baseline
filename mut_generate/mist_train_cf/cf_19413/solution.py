"""
QUESTION:
Create a function `is_prime_palindrome(num)` that takes an integer `num` as input and returns a boolean value indicating whether the number is a prime palindrome or not. A prime palindrome number is a number that is both prime and a palindrome. The function should check if the number is prime by iterating up to the square root of the number and then check if it is a palindrome by comparing the string representation of the number with its reverse. Return `True` if the number is a prime palindrome, and `False` otherwise.
"""

import math

def is_prime_palindrome(num):
    # Step 1: Check if the number is prime
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    
    # Step 2: Check if the number is a palindrome
    return str(num) == str(num)[::-1]