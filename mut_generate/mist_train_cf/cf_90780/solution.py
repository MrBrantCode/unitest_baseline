"""
QUESTION:
Write a function `convert_to_uppercase(string)` that takes a string as input and returns its uppercase equivalent without using any built-in string manipulation functions or methods. The function should handle both lowercase and non-letter characters.
"""

def convert_to_uppercase(string):
    uppercase_string = ""
    for char in string:
        if ord(char) >= 97 and ord(char) <= 122:
            uppercase_string += chr(ord(char) - 32)
        else:
            uppercase_string += char
    return uppercase_string