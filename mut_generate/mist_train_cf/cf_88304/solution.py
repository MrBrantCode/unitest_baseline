"""
QUESTION:
Write a function `convert_to_uppercase` that takes a string of up to 100 characters as input and returns a new string where all lowercase alphabetical characters are converted to uppercase, while non-alphabetical and already uppercase characters are excluded.
"""

def convert_to_uppercase(string):
    result = ""
    for char in string:
        if char.isalpha() and not char.isupper():
            result += char.upper()
    return result