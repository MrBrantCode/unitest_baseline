"""
QUESTION:
Create a function called `remove_punct` that takes a string as input and returns the string with all punctuation marks removed. The function should consider alphanumeric characters and whitespace as non-punctuation characters.
"""

import re

def remove_punct(string):
    return re.sub(r'[^\w\s]','',string)