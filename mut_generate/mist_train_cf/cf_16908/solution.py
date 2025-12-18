"""
QUESTION:
Create a function named `to_hexadecimal` that takes a number as input and returns its hexadecimal representation as a string. The input number can be negative or a decimal with up to 30 decimal places. The function should have a time complexity of O(n), where n is the number of decimal places in the input number, and a space complexity of O(1).
"""

def to_hexadecimal(number):
    # Step 1: Extract integer and decimal parts
    integer_part = abs(int(number))
    decimal_part = abs(number) - integer_part

    # Step 2: Convert integer part to hexadecimal
    hex_integer = hex(integer_part)[2:]

    # Step 3: Convert decimal part to hexadecimal
    hex_decimal = ''
    while decimal_part > 0 and len(hex_decimal) <= 30:
        decimal_part *= 16
        digit = int(decimal_part)
        hex_decimal += hex(digit)[2:]
        decimal_part -= digit

    # Step 4: Combine hexadecimal representations
    hexadecimal = hex_integer + '.' + hex_decimal if hex_decimal else hex_integer

    # Handle negative numbers
    if number < 0:
        hexadecimal = '-' + hexadecimal

    return hexadecimal.upper()