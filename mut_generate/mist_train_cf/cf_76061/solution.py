"""
QUESTION:
Write a function named `hex_to_ascii` that takes a string of hexadecimal digits as input, representing a UTF-8 encoded text, and returns its ASCII equivalent. The input string should be a valid hexadecimal representation, and the output should be a string containing the corresponding ASCII characters.
"""

def hex_to_ascii(hex_str):
    hex_bytes = bytes.fromhex(hex_str)
    return hex_bytes.decode('utf-8')