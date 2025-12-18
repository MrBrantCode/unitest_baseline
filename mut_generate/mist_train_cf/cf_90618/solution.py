"""
QUESTION:
Implement a function called "decimal_to_hexadecimal" that takes a decimal number as an argument and returns its hexadecimal equivalent as a string. The function should handle both positive and negative numbers, as well as decimal numbers with fractional parts. If the decimal number has a fractional part, the hexadecimal equivalent should be rounded to 2 decimal places. The implementation should not use any built-in functions or libraries for converting decimal to hexadecimal.
"""

def decimal_to_hexadecimal(decimal):
    if decimal == 0:
        return '0'
    
    # Handle negative numbers
    is_negative = False
    if decimal < 0:
        is_negative = True
        decimal = abs(decimal)
    
    # Separate the integer and fractional parts
    integer_part = int(decimal)
    fractional_part = decimal - integer_part
    
    # Convert the integer part to hexadecimal
    hexadecimal = ''
    while integer_part > 0:
        remainder = integer_part % 16
        if remainder < 10:
            hexadecimal = str(remainder) + hexadecimal
        else:
            hexadecimal = chr(ord('A') + remainder - 10) + hexadecimal
        integer_part = integer_part // 16
    
    # Add the fractional part if it exists
    if fractional_part > 0:
        hexadecimal += '.'
        # Convert the fractional part to hexadecimal
        count = 0
        while count < 2:
            fractional_part *= 16
            digit = int(fractional_part)
            if digit < 10:
                hexadecimal += str(digit)
            else:
                hexadecimal += chr(ord('A') + digit - 10)
            fractional_part -= digit
            count += 1
    
    # Add the negative sign if necessary
    if is_negative:
        hexadecimal = '-' + hexadecimal
    
    return hexadecimal