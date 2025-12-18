"""
QUESTION:
Write a function `transform_text` that takes a string as input and returns a string where all uppercase letters are converted to lowercase and all punctuation marks are replaced with spaces.
"""

import string

def transform_text(text):
    result = ''
    for char in text:
        if char.isupper() or char in string.punctuation:
            if char.isupper():
                result += char.lower()
            elif char in string.punctuation:
                result += ' '
        else:
            result += char
    return result