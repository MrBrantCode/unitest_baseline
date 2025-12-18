"""
QUESTION:
Write a function `trim_string(input_string)` that takes a string as input and returns the string with leading and trailing whitespace characters removed and consecutive whitespace characters replaced with a single space. The function should preserve punctuation marks and special characters in the final result.
"""

import re

def trim_string(input_string):
    # Remove leading and trailing whitespace characters
    trimmed_string = input_string.strip()

    # Remove consecutive whitespace characters within the string
    trimmed_string = re.sub(r'\s+', ' ', trimmed_string)

    return trimmed_string