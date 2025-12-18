"""
QUESTION:
Write a function `get_uppercase_chars` that takes a string as input and returns a string containing only the uppercase alphabetic characters from the input string, ignoring any non-alphabetic characters. The function should not use any built-in Python functions or libraries that directly solve the problem, such as `str.isupper()` or `str.upper()`.
"""

def entrance(input_string):
    result = ""
    for char in input_string:
        if 'A' <= char <= 'Z':
            result += char
    return result