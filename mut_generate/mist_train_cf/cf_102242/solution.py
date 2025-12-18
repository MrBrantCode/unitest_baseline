"""
QUESTION:
Write a function `convert_to_uppercase(string)` that takes a string of up to 100 characters as input, and returns a string with all lowercase alphabetical characters converted to uppercase, while leaving all non-alphabetical and already uppercase characters unchanged.
"""

def convert_to_uppercase(string):
    result = ""
    for char in string:
        if char.isalpha() and char.islower():
            result += char.upper()
        else:
            result += char
    return result