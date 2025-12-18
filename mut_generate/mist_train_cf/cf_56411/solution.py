"""
QUESTION:
Create a function called `hex_to_char` that takes a string representing a Unicode hexadecimal value as input and returns its corresponding Unicode character. The input string should not include the '0x' prefix or any escape characters. The function should be able to handle any valid Unicode hexadecimal value.
"""

def hex_to_char(hex_value):
    return chr(int(hex_value, 16))