"""
QUESTION:
Write a Python function named `check_numbers` that takes a string of space-separated numbers in scientific notation as input and returns True if all numbers in the string have a prime exponent and False otherwise. The function should assume that the input string is non-empty and contains at least one number. Each number in the string should be in the format of a decimal number (possibly with a leading negative sign) followed by 'e' and an integer exponent.
"""

import math

def check_numbers(string):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    numbers = string.split()
    for number in numbers:
        parts = number.split('e')
        if len(parts) != 2:
            return False
        mantissa = parts[0]
        exponent = int(parts[1])
        if not mantissa.replace('.', '').replace('-', '').isdigit():
            return False
        if not is_prime(abs(exponent)):
            return False
    return True