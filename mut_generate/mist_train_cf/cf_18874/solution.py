"""
QUESTION:
Create a function named `convert_to_uppercase` that takes a string as input and returns a string where all lowercase alphabetical characters are converted to uppercase, leaving all non-alphabetical characters and uppercase alphabetical characters unchanged.
"""

def convert_to_uppercase(string):
    converted_string = ""
    for char in string:
        if char.isalpha() and not char.isupper():
            converted_string += char.upper()
        else:
            converted_string += char
    return converted_string