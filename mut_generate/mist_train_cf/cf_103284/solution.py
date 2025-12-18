"""
QUESTION:
Write a function `convert_to_lowercase` that takes a string as input and returns the string with all alphabetic characters converted to lowercase, leaving non-alphabetic characters (such as numbers and special characters) unchanged.
"""

def convert_to_lowercase(string):
    new_string = ""
    for char in string:
        if char.isalpha():
            new_string += char.lower()
        else:
            new_string += char
    return new_string