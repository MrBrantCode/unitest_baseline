"""
QUESTION:
Write a function named `trim_string` that takes a string as input, removes leading and trailing whitespace characters, and replaces any consecutive whitespace characters within the string with a single space.
"""

import re

def trim_string(input_string):
    return re.sub(r'\s+', ' ', input_string).strip()