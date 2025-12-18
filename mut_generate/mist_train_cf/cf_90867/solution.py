"""
QUESTION:
Write a function named `extract_digits` that takes a number (up to 10^15, can be positive or negative, and may contain decimal points) as input and returns an array of its digits. If the number is negative, include a '-' symbol at the beginning of the array.
"""

def extract_digits(number):
    number_str = str(number)
    is_negative = False
    if number_str.startswith('-'):
        is_negative = True
        number_str = number_str[1:]
    parts = number_str.split('.')
    integer_part = parts[0]
    decimal_part = parts[1] if len(parts) > 1 else ''
    integer_digits = [int(digit) for digit in integer_part]
    decimal_digits = [int(digit) for digit in decimal_part]
    digits = integer_digits + decimal_digits
    if is_negative:
        digits.insert(0, '-')
    return digits