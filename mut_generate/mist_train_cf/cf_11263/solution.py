"""
QUESTION:
Write a function `remove_trailing_spaces` that takes an input string containing alphanumeric characters, spaces, and punctuation, and returns the input string with all trailing spaces removed without using any built-in string manipulation functions or libraries.
"""

def remove_trailing_spaces(input_string):
    i = len(input_string) - 1
    while i >= 0 and input_string[i] == ' ':
        i -= 1
    return input_string[:i+1]