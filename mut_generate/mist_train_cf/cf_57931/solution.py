"""
QUESTION:
Write a function `replace_exclamation_and_uppercase` that takes a string `s` as input, replaces all exclamation marks with underscores, and replaces all capital letters with their ASCII codes. Return the resulting string without using built-in string functions or any additional libraries.
"""

def replace_exclamation_and_uppercase(s):
    result = ""
    for char in s:
        if char == "!":
            result += "_"
        elif char.isupper():
            result += str(ord(char))  # Convert the capital letters to their ASCII codes.
        else:
            result += char
    return result