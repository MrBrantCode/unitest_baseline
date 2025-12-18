"""
QUESTION:
Write a function `remove_odd_characters` that takes a string as input and returns the modified string with characters at odd index values removed, excluding any punctuation marks. The function should handle leading and trailing whitespace characters and preserve the original casing of the characters.
"""

import string

def remove_odd_characters(s):
    s = s.strip()
    s = s.translate(str.maketrans('', '', string.punctuation))
    modified_string = ''
    for index, char in enumerate(s):
        if index % 2 == 0:
            modified_string += char
    return modified_string