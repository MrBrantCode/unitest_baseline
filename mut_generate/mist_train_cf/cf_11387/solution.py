"""
QUESTION:
Write a function `convert_to_uppercase` that takes a string as input and returns a new string where all lowercase letters are converted to uppercase. The function should not use the built-in `upper()` or `islower()` methods.
"""

def convert_to_uppercase(s):
    modified_string = ""
    for char in s:
        if ord(char) >= 97 and ord(char) <= 122:
            modified_string += chr(ord(char) - 32)
        else:
            modified_string += char
    return modified_string