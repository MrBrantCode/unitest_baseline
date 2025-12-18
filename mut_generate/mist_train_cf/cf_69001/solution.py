"""
QUESTION:
Create a function named `hex_to_oct(hex_val)` that takes a hexadecimal number as input and returns its equivalent octal representation as a string. The function should first convert the hexadecimal number to decimal and then convert the decimal to octal. Note that the returned octal value should be a string and may have a leading "0o" to indicate it's an octal number.
"""

def hex_to_oct(hex_val):
    # Convert Hexadecimal to Decimal
    dec_val = int(hex_val, 16)
    
    # Convert Decimal to Octal
    oct_val = oct(dec_val)
    return oct_val