"""
QUESTION:
Write a function named `is_scientific_notation_with_prime_exponent` that checks if a given string represents a number in scientific notation with a prime exponent. The function should return True if the string is in scientific notation and the exponent is a prime number, and False otherwise.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_scientific_notation_with_prime_exponent(s):
    try:
        float(s)  
        parts = s.split('e')
        if len(parts) != 2:
            return False
        exponent = int(parts[1])
        if not is_prime(abs(exponent)):
            return False
        return True
    except ValueError:
        return False