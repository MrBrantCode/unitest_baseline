"""
QUESTION:
Create a function `to_hexadecimal(number)` that takes a single argument `number`, a floating point number, and returns its hexadecimal representation as a string. The function should handle numbers with up to 30 decimal places accurately, have a time complexity of O(n), where n is the number of decimal places in the input number, and have a space complexity of O(1). The function should also handle negative numbers correctly by prefixing the hexadecimal representation with a minus sign.
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