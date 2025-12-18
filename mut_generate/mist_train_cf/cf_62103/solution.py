"""
QUESTION:
Create a function `remove_punctuation(input_string)` that takes a string as input and returns the string with all punctuation marks removed, excluding question marks and exclamation points. The function should maintain the original sequence of non-alphanumeric characters.
"""

import string

def remove_punctuation(input_string):
    exclude = set(string.punctuation) - set(['?', '!'])
    no_punct = ""
    for char in input_string:
        if char not in exclude:
            no_punct = no_punct + char
    return no_punct