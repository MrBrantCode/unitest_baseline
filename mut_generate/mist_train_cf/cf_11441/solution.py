"""
QUESTION:
Write a function named `is_armstrong_number` that takes one argument, an integer. The function should return `True` if the number is prime and has exactly three unique digits, and `False` otherwise.
"""

import math

def is_armstrong_number(number):
    # Check if the number is prime
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    # Check if the number has exactly three unique digits
    digit_set = set(str(number))
    if len(digit_set) != 3:
        return False

    # If both conditions are met, return True
    return True