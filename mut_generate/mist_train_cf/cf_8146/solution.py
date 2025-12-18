"""
QUESTION:
Create a function named `is_prime` that takes an integer as input and returns `True` if the number is prime, and `False` otherwise. The function should efficiently determine if a number is prime or not without relying on pre-calculated prime numbers list or brute force checking. The function should be able to handle numbers up to the maximum limit of the programming language's integer data type.
"""

import math

def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    else:
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True