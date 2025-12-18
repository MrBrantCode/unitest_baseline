"""
QUESTION:
Write a function `check_string` that takes a string `s` as input. The function should return the type of notation ('Decimal', 'Scientific', or 'Hexadecimal') if the string represents a positive decimal number with a precision of up to 8 decimal places and falls within the range [0, 1000000], including numbers in scientific and hexadecimal notation. Otherwise, return 'Invalid'.
"""

import decimal

def check_string(s):
    try:
        # check if the string can be converted to a decimal number with precision of upto 8 decimal places
        decimal_val = decimal.Decimal(s)
        decimal_val = round(decimal_val, 8)
        float_val = float(decimal_val)
        if float_val >= 0 and float_val <= 1000000:
            # check for scientific notation
            if 'e' in s or 'E' in s:
                return 'Scientific'
            # check for hexadecimal notation
            elif 'x' in s or 'X' in s:
                return 'Hexadecimal'
            else:
                return 'Decimal'
        else:
            return 'Invalid'
    except decimal.InvalidOperation:
        return 'Invalid'