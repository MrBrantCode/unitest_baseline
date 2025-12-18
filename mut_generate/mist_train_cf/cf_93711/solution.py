"""
QUESTION:
Write a function `is_scientific_notation_with_prime_exponent(s)` that takes a string `s` as input and returns `True` if the string represents a number in scientific notation with a prime exponent, and `False` otherwise. The function should check if the string can be converted to a float and if the exponent part is a prime number.
"""

import math

def is_scientific_notation_with_prime_exponent(s):
    try:
        float(s)  # check if the string can be converted to a float
        parts = s.split('e')
        if len(parts) != 2:
            return False
        exponent = int(parts[1])
        if exponent < 2:
            return False
        for i in range(2, int(math.sqrt(exponent)) + 1):
            if exponent % i == 0:
                return False
        return True
    except ValueError:
        return False