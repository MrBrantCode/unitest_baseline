"""
QUESTION:
Write a function `ascii_to_dec(input_string)` that converts a given string of ASCII characters to their equivalent decimal values, ignoring case and whitespace characters, and returns the XOR of these decimal values.
"""

def ascii_to_dec(input_string):
    value = 0
    for char in input_string.lower(): 
        if char != ' ': 
            value ^= ord(char)
    return value