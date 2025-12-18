"""
QUESTION:
Write a function named `get_uppercase_chars` that takes a string `input_string` as input. The function should return a string containing only the uppercase alphabetic characters from the input string, ignoring any non-alphabetic characters. The function should not use built-in Python functions or libraries that directly solve the problem.
"""

def get_uppercase_chars(input_string):
    uppercase_chars = ''
    for char in input_string:
        if 'A' <= char <= 'Z':
            uppercase_chars += char
    return uppercase_chars