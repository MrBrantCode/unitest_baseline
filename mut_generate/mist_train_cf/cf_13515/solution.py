"""
QUESTION:
Write a function `to_uppercase(s)` that converts a given string `s` to all uppercase letters without using the built-in `upper()` function. The function should handle both lowercase and uppercase letters, as well as non-alphabetic characters.
"""

def entrance(s):
    uppercase_str = ""
    for char in s:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - 32)
        else:
            uppercase_char = char
        uppercase_str += uppercase_char
    return uppercase_str