"""
QUESTION:
Write a function `convert_to_lowercase_with_underscores` that takes a string as input and returns a new string where all letters are converted to lowercase and all non-alphabetic characters (including spaces, punctuation marks, and special characters) are replaced with underscores.
"""

def convert_to_lowercase_with_underscores(string):
    lowercase_string = string.lower()
    converted_string = ""

    for char in lowercase_string:
        if char.isalpha():
            converted_string += char
        else:
            converted_string += "_"

    return converted_string