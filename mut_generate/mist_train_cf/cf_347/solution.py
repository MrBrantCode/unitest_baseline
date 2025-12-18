"""
QUESTION:
Implement a function named `check_numbers` that takes a string of numbers as input, where the numbers are separated by whitespace and are in scientific notation with an exponent. The function should return True if all numbers in the string satisfy the conditions that they are in scientific notation and have a prime exponent, and False otherwise. The numbers can have a decimal point and a negative sign.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def check_numbers(string):
    numbers = string.split()
    for number in numbers:
        parts = number.split('e')
        if len(parts) != 2:
            return False
        mantissa = parts[0]
        exponent = int(parts[1])
        if not mantissa.replace('.', '').replace('-', '', 1).isdigit():
            return False
        if not is_prime(exponent):
            return False
    return True