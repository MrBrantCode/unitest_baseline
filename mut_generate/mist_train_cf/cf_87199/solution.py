"""
QUESTION:
Implement a function named `convert_to_ascii` that takes a string as input and returns a list of integers representing the UTF-8 byte values of the characters in the input string. The function should correctly handle all characters, including Unicode characters, without using any built-in string manipulation functions or libraries.
"""

def convert_to_ascii(string):
    result = []
    encoded_string = string.encode('utf-8')
    for byte in encoded_string:
        result.append(byte)
    return result