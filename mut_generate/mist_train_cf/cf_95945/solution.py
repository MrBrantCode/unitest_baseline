"""
QUESTION:
Write a function `get_uppercase_chars` that takes a string as input and returns a string containing only the uppercase alphabetic characters from the input string, ignoring any punctuation or whitespace characters. Do not use built-in Python functions or libraries that directly solve the problem, such as `str.isupper()` or `str.upper()`.
"""

def get_uppercase_chars(input_string):
    uppercase_chars = ""
    for char in input_string:
        if char.isalpha() and char.isupper():
            uppercase_chars += char
    return uppercase_chars