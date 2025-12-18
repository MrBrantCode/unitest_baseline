"""
QUESTION:
Write a function called `remove_non_alphanumeric` that takes a string as input, removes any non-alphanumeric characters, and returns the modified string. The input string will only contain printable ASCII characters.
"""

import re

def remove_non_alphanumeric(string):
    # Remove non-alphanumeric characters and special characters within alphanumeric characters
    modified_string = re.sub(r'\W+', '', string)
    return modified_string