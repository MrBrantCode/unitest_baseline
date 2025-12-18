"""
QUESTION:
Create a function called `alphanumeric_to_hexadecimal` that takes a string of alphanumeric characters as input and returns a string representing the hexadecimal equivalent of each character in the input sequence. The function should use the Unicode point of each character to calculate its hexadecimal representation. The function should work with Unicode characters less than or equal to `FFFF` (or `10000` in decimal).
"""

def alphanumeric_to_hexadecimal(input_sequence):
    return ''.join([hex(ord(c))[2:] for c in input_sequence])