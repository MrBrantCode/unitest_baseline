"""
QUESTION:
Write a function `remove_special_chars` that takes a string as input and returns the modified string without any special characters or uppercase letters. The function should keep the '@' symbol and convert all letters to lowercase. Special characters include any character that is not a letter, number, or the '@' symbol.
"""

import re

def remove_special_chars(string):
    # Remove all special characters, except for '@'
    string = re.sub('[^a-zA-Z0-9@]', '', string)
    
    # Convert all uppercase letters to lowercase
    string = string.lower()
    
    return string