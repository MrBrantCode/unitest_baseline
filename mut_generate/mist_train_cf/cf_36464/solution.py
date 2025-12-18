"""
QUESTION:
Write a function `hexToAscii` that takes a string of hexadecimal values, where each pair of hexadecimal values represents a single byte, as input and returns the decoded ASCII string. The input string is in the format of a sequence of bytes in hexadecimal, prefixed with '\x'. The function should be able to handle any valid input string in this format and return the corresponding ASCII representation.
"""

def hexToAscii(hex_string):
    hex_values = hex_string.split('\\x')[1:]  # Split the string by '\x' and remove the empty first element
    ascii_string = ''.join(chr(int(hex_val, 16)) for hex_val in hex_values)  # Convert each hex value to ASCII character
    return ascii_string