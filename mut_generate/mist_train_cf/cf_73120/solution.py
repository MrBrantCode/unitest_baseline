"""
QUESTION:
Create a function `is_prime` that checks whether a number is prime or not. The function should return `True` for prime numbers and `False` for non-prime numbers. Restrict the input to integers. Optimize the function to check for divisibility up to the square root of the input number.

Create a dictionary with keys as prime numbers from 1 to 50 and values as their 10th power using the `is_prime` function in a dictionary comprehension.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    elif n == 2: 
        return True
    elif n % 2 == 0: 
        return False
    else:
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True