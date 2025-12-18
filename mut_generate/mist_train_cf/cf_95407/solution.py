"""
QUESTION:
Write a function named `convert_to_uppercase` that takes a string as input, iterates over each character, and converts it to uppercase if the character is alphabetical and not already uppercase. Non-alphabetical characters and already uppercase characters should remain unchanged. Return the modified string.
"""

def convert_to_uppercase(string):
    converted_string = ""
    for char in string:
        if char.isalpha() and not char.isupper():
            converted_string += char.upper()
        else:
            converted_string += char
    return converted_string