"""
QUESTION:
Design a function `hex_to_oct` that converts a given hexadecimal number into its octal representation. The function should take a string of hexadecimal digits as input and return a string of octal digits. The input hexadecimal number is between 1 and 15 in hexadecimal representation.
"""

def hex_to_oct(hex_val):
    # converting hexadecimal to decimal
    dec_val = int(hex_val, 16)
    
    # converting decimal to octal
    oct_val = oct(dec_val)
    
    # removing '0o' from the output string
    return oct_val[2:]