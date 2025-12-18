"""
QUESTION:
Implement a function `to_lower_case(s)` that converts the input string `s` to an all lowercase string without using any built-in string manipulation functions or methods such as `toLowerCase()` or `lower()`. The function should return the converted string.
"""

def to_lower_case(s):
    result = ""
    for char in s:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result