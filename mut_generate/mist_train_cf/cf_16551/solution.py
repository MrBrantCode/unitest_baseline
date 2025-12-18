"""
QUESTION:
Write a Python function `to_uppercase` that takes a string as input and returns the string with all letters converted to uppercase without using any built-in string manipulation methods. The function should handle strings containing special characters and numbers, keeping them unchanged.
"""

def to_uppercase(s):
    result = ''
    for char in s:
        char_code = ord(char)
        if 97 <= char_code <= 122: 
            result += chr(char_code - 32) 
        else:
            result += char
    return result