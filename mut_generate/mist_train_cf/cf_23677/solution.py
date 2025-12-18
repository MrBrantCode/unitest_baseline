"""
QUESTION:
Create a function called `string_to_hexadecimal` that takes a string as input and returns the hexadecimal representation of the string. The output should be a single string where each character in the input string is represented by its corresponding hexadecimal code without the "0x" prefix.
"""

def string_to_hexadecimal(string):
    return ''.join(hex(ord(char))[2:] for char in string)