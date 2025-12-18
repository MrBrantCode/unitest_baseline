"""
QUESTION:
Write a function named `string_to_hex` that takes a string of up to 100 characters as input. The function should return a string with the hexadecimal representation of the input string, ignoring non-alphanumeric characters, handling both uppercase and lowercase letters, and converting special characters to their ASCII values in hexadecimal representation. The output should be in lowercase.
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