"""
QUESTION:
Write a function `convert_to_uppercase` that takes a string as input and converts each character to uppercase. The function should return the modified string. Note that you are not allowed to use any built-in functions or libraries for string manipulation, such as `upper()`, `lower()`, `isupper()`, `islower()`, `chr()`, and `ord()`, that directly handle string case conversion.
"""

def convert_to_uppercase(string):
    uppercase_string = ""
    for char in string:
        if ord('a') <= ord(char) <= ord('z'):
            uppercase_string += chr(ord(char) - 32)
        else:
            uppercase_string += char
    return uppercase_string