"""
QUESTION:
Create a function named `regex_match` that performs a regular expression match on a given string. The function should return the first match found at the beginning of the string, ignoring any subsequent matches, or return `None` if no match is found.
"""

import re

def regex_match(pattern, string):
    match = re.match(pattern, string)
    return match.group(0) if match else None