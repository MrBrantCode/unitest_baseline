"""
QUESTION:
Create a function `validate_string(s)` that takes a string `s` as input and returns a boolean indicating whether the string contains the characters 'a', 'b', and 'c' in order, possibly separated by other characters. The function should return True if the characters appear in the correct order, and False otherwise.
"""

import re

def validate_string(s):
    regex = r'^.*a.*b.*c.*$'
    match = re.search(regex, s)
    if match:
        return True
    return False