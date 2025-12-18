"""
QUESTION:
Design a Python function `hex_to_ascii(hex_value)` that takes a distinct hexadecimal representation as input and returns its corresponding ASCII character. The input hexadecimal value should be converted to decimal using base 16, and then transformed into its corresponding ASCII character. The function should handle valid hexadecimal inputs only.
"""

def hex_to_ascii(hex_value):
    ascii_value = int(hex_value, 16)
    return chr(ascii_value)