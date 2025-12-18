"""
QUESTION:
Develop a function named `remove_special_characters` that takes a string as input and returns a new string with all non-alphanumeric characters removed, except for spaces. The function should use regular expressions and allow for customization of the filter by modifying the pattern.
"""

import re

def remove_special_characters(input_str):
    # Replace non-alphanumeric characters with an empty string
    result = re.sub(r'[^a-zA-Z0-9 ]', '', input_str)
    return result