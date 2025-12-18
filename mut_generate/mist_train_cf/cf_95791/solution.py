"""
QUESTION:
Write a function named `string_to_hex` that takes a string as input, converts it to its hexadecimal representation, and returns the result as a string with lowercase hexadecimal characters. The function should ignore any non-alphanumeric characters and handle special characters by converting them to their corresponding ASCII values in hexadecimal representation. The input string must not exceed 100 characters in length.
"""

def string_to_hex(string):
    if len(string) > 100:
        return "Input string should not exceed 100 characters."
    
    hex_string = ""
    
    for char in string:
        if char.isalnum():
            hex_string += hex(ord(char))[2:]
        else:
            hex_string += hex(ord(char))[2:].zfill(2)
    
    return hex_string.lower()