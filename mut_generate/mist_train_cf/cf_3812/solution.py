"""
QUESTION:
Write a function named `base10_to_base16` that takes a number as input and returns its equivalent in base 16 as a string. The function should handle negative numbers, floating-point numbers, and special cases such as zero, negative zero, infinity, and NaN. If the input is not a valid number, the function should return an error message.
"""

import sys

def base10_to_base16(number):
    # Check if the input is a valid number
    try:
        number = float(number)
    except ValueError:
        return "Invalid input. Please enter a valid number."

    # Handle special cases
    if number == 0:
        return "0"
    elif number == -0:
        return "-0"
    elif number == float('inf'):
        return "Infinity"
    elif number == float('-inf'):
        return "-Infinity"
    elif number != number:
        return "NaN"

    # Handle negative numbers
    is_negative = False
    if number < 0:
        is_negative = True
        number = abs(number)

    # Convert the integer part to base 16
    integer_part = int(number)
    base16_integer = hex(integer_part)[2:]

    # Convert the decimal part to base 16
    decimal_part = number - integer_part
    base16_decimal = ""
    while decimal_part != 0 and len(base16_decimal) < 16:  # Limit decimal places to 16
        decimal_part *= 16
        digit = int(decimal_part)
        base16_decimal += str(digit)
        decimal_part -= digit

    # Combine the integer and decimal parts
    base16_number = base16_integer
    if base16_decimal:
        base16_number += "." + base16_decimal

    # Add the negative sign if necessary
    if is_negative:
        base16_number = "-" + base16_number

    return base16_number