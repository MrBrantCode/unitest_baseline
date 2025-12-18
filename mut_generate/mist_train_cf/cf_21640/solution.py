"""
QUESTION:
Create a function called `remove_spaces_and_punctuation` that takes a string as input and returns a new string with all blank spaces and punctuation marks removed, while preserving the original order of characters. The function should not leave any blank spaces in the resulting string.
"""

import re

def remove_spaces_and_punctuation(string):
    # Remove blank spaces and punctuation marks
    cleaned_string = re.sub(r'[^\w]', '', string)
    return cleaned_string