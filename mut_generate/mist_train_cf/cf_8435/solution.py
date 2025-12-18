"""
QUESTION:
Write a function called `calculate_sum` that takes an input string representing an integer and returns the sum of the absolute values of its digits. The input string may be negative, contain a decimal point, be in scientific notation, have leading zeros, contain special characters or alphabetic characters, or be in a non-English numeric system. The function should ignore special characters, leading zeros, and alphabetic characters, and handle negative signs, decimal points, and scientific notation correctly.
"""

import re

def calculate_sum(input_integer):
    # Remove special characters, leading zeros, and alphabetic characters
    cleaned_integer = re.sub('[^0-9.-]', '', input_integer).lstrip('0')

    # Check if the input is negative
    is_negative = False
    if cleaned_integer.startswith('-'):
        is_negative = True
        cleaned_integer = cleaned_integer[1:]

    # Split into integer and decimal parts (if any)
    parts = cleaned_integer.split('.')
    integer_part = parts[0]
    decimal_part = parts[1] if len(parts) > 1 else ''

    # Calculate sum of absolute values of digits in the integer part
    integer_sum = sum([int(digit) for digit in integer_part])

    # Calculate sum of absolute values of digits in the decimal part
    decimal_sum = sum([int(digit) for digit in decimal_part])

    # Calculate sum of absolute values of digits in the exponent part (if scientific notation)
    exponent_sum = 0
    if 'e' in cleaned_integer:
        exponent = cleaned_integer.split('e')[1]
        exponent_sum = sum([int(digit) for digit in exponent])

    # Calculate sum including all parts
    total_sum = integer_sum + decimal_sum + exponent_sum

    # Add negative sign if necessary
    if is_negative:
        total_sum = -total_sum

    return total_sum