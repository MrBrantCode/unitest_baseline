"""
QUESTION:
Extract the digits from a given number as an array. The function, `extract_digits(number)`, should handle numbers up to 10^15, including both positive and negative numbers with decimal points. The output array should contain the digits of the number in the order they appear, with a '-' at the beginning if the number is negative, and a '.' in its original position if the number is a decimal.
"""

def extract_digits(number):
    # Convert the number to a string
    number_str = str(number)

    # Check if the number is negative
    is_negative = False
    if number_str.startswith('-'):
        is_negative = True
        number_str = number_str[1:]

    # Split the number into integer and decimal parts
    parts = number_str.split('.')
    integer_part = parts[0]
    decimal_part = parts[1] if len(parts) > 1 else ''

    # Extract the digits from the integer part
    integer_digits = [int(digit) for digit in integer_part]

    # Extract the digits from the decimal part
    decimal_digits = [int(digit) for digit in decimal_part]

    # Combine the digits into a single array
    digits = integer_digits + ([float('inf')] if decimal_part else []) + decimal_digits

    # Add the sign if the number was negative
    if is_negative:
        digits.insert(0, '-')

    return digits