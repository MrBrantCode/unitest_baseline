"""
QUESTION:
Create a function named `decimal_to_hexadecimal` that takes one argument `number` and converts any negative or decimal number to its hexadecimal representation. The function should handle numbers with up to 15 decimal places accurately.
"""

def decimal_to_hexadecimal(number):
    is_negative = False
    if number < 0:
        is_negative = True
        number = abs(number)

    integer_part = int(number)
    decimal_part = number - integer_part

    hex_integer = hex(integer_part)[2:]  

    hex_decimal = ''
    while decimal_part > 0 and len(hex_decimal) < 15:
        decimal_part *= 16
        hex_digit = hex(int(decimal_part))[2:]  
        hex_decimal += hex_digit
        decimal_part -= int(decimal_part)

    hexadecimal = hex_integer
    if hex_decimal:
        hexadecimal += '.' + hex_decimal

    if is_negative:
        hexadecimal = '-' + hexadecimal

    return hexadecimal