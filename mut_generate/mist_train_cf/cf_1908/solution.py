"""
QUESTION:
Implement a function named `convert_to_ascii` that takes a string as input and returns a list of integers representing the UTF-8 byte values of the characters in the input string. The function should handle all characters, including Unicode characters. Do not use any built-in functions or libraries for string manipulation, except for the `encode` method of strings.
"""

def convert_to_ascii(s):
    result = []
    encoded_string = s.encode('utf-8')
    for byte in encoded_string:
        result.append(byte)
    return result