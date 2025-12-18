"""
QUESTION:
Write a function named `is_prime` that takes an integer as input and returns `True` if the number is prime, `False` otherwise. Use this function to parse a given text, extract numbers, and identify prime numbers among them. The function should not take any input parameters, but the code that calls it will include a predefined text string. The prime numbers should be printed as output.
"""

import re

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n%2 == 0 or n%3 == 0:
        return False
    i = 5
    while (i * i <= n):
        if (n%i == 0 or n%(i + 2) == 0):
            return False
        i += 6
    return True