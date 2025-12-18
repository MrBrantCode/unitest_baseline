"""
QUESTION:
Create a function named `strip_spaces` that takes a string as input, removes all spaces from the string, and returns the resulting string without using any built-in string manipulation functions or libraries.
"""

def strip_spaces(string):
    stripped_string = ''
    for char in string:
        if char != ' ':
            stripped_string += char
    return stripped_string