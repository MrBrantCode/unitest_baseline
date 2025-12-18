"""
QUESTION:
Create a function `is_prime` that checks if a given number is prime. Use this function to find all prime numbers from 1 to 1000 inclusive. The function should return a boolean value for a single input number and your solution should be implemented in Python.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True