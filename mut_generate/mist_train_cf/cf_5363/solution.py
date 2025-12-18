"""
QUESTION:
Write a function named `get_lowercase` that takes an input string and returns a string containing only the lowercase alphabetic characters from the input string. The function should not use any built-in Python functions or libraries that directly solve the problem, such as `str.islower()` or `str.lower()`.
"""

def get_lowercase(input_string):
    lowercase_chars = ""
    for char in input_string:
        if 'a' <= char <= 'z':
            lowercase_chars += char
    return lowercase_chars