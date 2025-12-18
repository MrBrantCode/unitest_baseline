"""
QUESTION:
Write a function called `base16_to_integer` that takes a string of hexadecimal digits as input and returns its corresponding integer value in base 10. The input string will only contain the characters '0'-'9' and 'A'-'F', which represent the hexadecimal digits 0-15.
"""

def base16_to_integer(s):
    hex_digits = '0123456789ABCDEF'
    decimal_value = 0
    for digit in s:
        decimal_value = decimal_value * 16 + hex_digits.index(digit)
    return decimal_value