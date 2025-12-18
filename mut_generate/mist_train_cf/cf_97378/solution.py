"""
QUESTION:
Create a function named `trim_string` that takes a string as input and returns the string with leading and trailing whitespace characters removed and any consecutive whitespace characters within the string replaced with a single space. The function should preserve punctuation marks and special characters in the final result.
"""

import re

def trim_string(input_string):
    trimmed_string = input_string.strip()
    trimmed_string = re.sub(r'\s+', ' ', trimmed_string)
    return trimmed_string