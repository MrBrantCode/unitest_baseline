"""
QUESTION:
Write a function `convert_to_upper` that takes a string as input and returns a new string in upper case. The function should handle all types of characters, including special characters and non-alphabetic characters, and should be case-sensitive. The function should not modify the original string and should not use any built-in functions or methods that directly convert a string to upper case.
"""

def convert_to_upper(string):
    result = ""
    for char in string:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result