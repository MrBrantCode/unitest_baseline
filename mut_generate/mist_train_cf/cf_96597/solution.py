"""
QUESTION:
Create a function `replace_characters` that takes a string and a dictionary of character replacements as input. The function should replace specified characters in the string while ignoring any non-ASCII characters and maintaining the original case of the replaced characters.
"""

import unicodedata

def replace_characters(string, replacements):
    result = ""
    for char in string:
        if ord(char) > 127:  
            continue
        normalized_char = unicodedata.normalize("NFKD", char)
        if normalized_char in replacements:
            result += replacements[normalized_char]
        else:
            result += char
    return result