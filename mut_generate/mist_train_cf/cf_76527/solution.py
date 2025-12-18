"""
QUESTION:
Create a function called `decimal_to_hex` that converts decimal numbers, including negative and floating-point numbers, into their hexadecimal equivalents. The function should return a string representation of the hexadecimal value, and it should exclude the '0x' prefix. The function should also handle negative numbers by adding a negative sign at the start of the hexadecimal value.
"""

def decimal_to_hex(number):
    if isinstance(number, float):
        return float.hex(number).replace('0x', '').replace('p', 'P')
    else:
        if number < 0:
            return '-' + hex(abs(number))[2:]
        else:
            return hex(number)[2:]