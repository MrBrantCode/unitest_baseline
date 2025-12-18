"""
QUESTION:
Create a function named `decimal_to_hexadecimal` that takes a single argument `number` and returns its hexadecimal representation. The function should handle negative numbers and decimal numbers with up to 15 decimal places accurately, converting the integer part using the `hex()` function and the decimal part by repeatedly multiplying by 16 and extracting the integer part.
"""

def decimal_to_hexadecimal(number):
    # Check if the number is negative
    is_negative = False
    if number < 0:
        is_negative = True
        number = abs(number)

    # Separate the integer and decimal parts
    integer_part = int(number)
    decimal_part = number - integer_part

    # Convert the integer part to hexadecimal
    hex_integer = hex(integer_part)[2:]  # Remove '0x' prefix

    # Convert the decimal part to hexadecimal
    hex_decimal = ''
    while decimal_part > 0 and len(hex_decimal) < 15:
        decimal_part *= 16
        hex_digit = hex(int(decimal_part))[2:]  # Remove '0x' prefix
        hex_decimal += hex_digit
        decimal_part -= int(decimal_part)

    # Combine the integer and decimal parts of the hexadecimal representation
    hexadecimal = hex_integer
    if hex_decimal:
        hexadecimal += '.' + hex_decimal

    # Add the minus sign for negative numbers
    if is_negative:
        hexadecimal = '-' + hexadecimal

    return hexadecimal