"""
QUESTION:
Create a function called `convert_to_hex` that takes a single argument `num`, a decimal number. The function should return the hexadecimal representation of `num`. The input `num` can be negative and have up to 30 decimal places. The function should have a time complexity of O(n), where n is the number of decimal places in `num`, and a space complexity of O(1).
"""

def convert_to_hex(num):
    # Check if the number is negative
    is_negative = False
    if num < 0:
        is_negative = True
        num = abs(num)

    # Separate the integer and fractional parts
    integer_part = int(num)
    fractional_part = num - integer_part

    # Convert the integer part to hexadecimal
    hex_integer = hex(integer_part)[2:]

    # Convert the fractional part to hexadecimal
    hex_fractional = ""
    while fractional_part > 0 and len(hex_fractional) < 30:  # Handle up to 30 decimal places
        fractional_part *= 16
        hex_digit = int(fractional_part)
        hex_fractional += hex(hex_digit)[2:]
        fractional_part -= hex_digit

    # Concatenate the hexadecimal representations
    hex_number = hex_integer
    if hex_fractional:
        hex_number += "." + hex_fractional

    # Add negative sign if necessary
    if is_negative:
        hex_number = "-" + hex_number

    return hex_number.upper()