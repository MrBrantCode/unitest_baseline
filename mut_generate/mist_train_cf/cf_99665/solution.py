"""
QUESTION:
Write a function `to_uppercase` that converts a given string to uppercase letters without using the `upper()` or `capitalize()` methods. The function should take a string as input and return the converted string in uppercase.
"""

def to_uppercase(string):
    uppercase = ""
    for char in string:
        if 97 <= ord(char) <= 122:
            uppercase += chr(ord(char) - 32)
        else:
            uppercase += char
    return uppercase