"""
QUESTION:
Create a function named `replace_characters` that takes a string and a dictionary of character replacements as input. The function should replace specified characters in the string while ignoring any non-ASCII characters and maintaining the original case of the replaced characters.
"""

import unicodedata

def replace_characters(string, replacements):
    result = ""
    for char in string:
        if ord(char) > 127:  # ignore non-ASCII characters
            continue
        if char.lower() in replacements:
            if char.isupper():
                result += replacements[char.lower()].upper()
            else:
                result += replacements[char.lower()]
        else:
            result += char
    return result