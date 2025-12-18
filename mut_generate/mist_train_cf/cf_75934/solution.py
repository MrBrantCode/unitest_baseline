"""
QUESTION:
Create a function named `to_hexadecimal` that converts a given string of characters into its equivalent hexadecimal notation. The function should accept a string as input, handle special characters, and return a string of hexadecimal values. If the input is not a string, the function should return an "Error: Invalid input. Please input a string" message. The function should also handle any invalid characters in the string and return an "Error: Invalid character in string" message.
"""

def to_hexadecimal(input_string):
    if not isinstance(input_string, str):
        return "Error: Invalid input. Please input a string"
    try:
        return ''.join(hex(ord(c))[2:] for c in input_string)
    except ValueError:
        return "Error: Invalid character in string"