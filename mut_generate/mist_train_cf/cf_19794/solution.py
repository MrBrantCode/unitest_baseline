"""
QUESTION:
Write a function called `change_case` that takes an input string and returns a new string with the case of all alphabetic characters changed, while leaving punctuation and other non-alphabetic characters unchanged.
"""

import string

def change_case(input_string):
    result = ""
    for char in input_string:
        if char.isalpha():
            if char.isupper():
                result += char.lower()
            else:
                result += char.upper()
        else:
            result += char
    return result