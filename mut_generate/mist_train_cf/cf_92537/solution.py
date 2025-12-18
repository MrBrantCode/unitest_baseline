"""
QUESTION:
Write a function `strip_spaces(string)` that takes a string as input and returns a new string with all spaces removed from the input string. The function should not use any built-in string manipulation functions or libraries.
"""

def strip_spaces(string):
    stripped_string = ''
    for char in string:
        if char != ' ':
            stripped_string += char
    return stripped_string