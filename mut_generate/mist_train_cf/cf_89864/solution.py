"""
QUESTION:
Create a function called `is_prime(num)` that takes a single integer argument and returns `True` if the number is prime and `False` otherwise. Use this helper function in a loop to print the square of each prime number from 0 to 100.
"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True