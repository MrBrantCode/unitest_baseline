"""
QUESTION:
Write a function `convert_camel_case(camel_case_string)` that takes a camel case string as input and returns a space-separated string while preserving the original casing of the words. The function should not use any built-in string manipulation methods or regular expressions.
"""

def convert_camel_case(camel_case_string):
    space_separated = ''
    for char in camel_case_string:
        if ord(char) >= 65 and ord(char) <= 90:  # ASCII values for A-Z
            space_separated += ' ' 
        space_separated += char
    return space_separated