"""
QUESTION:
Create a function `validate_string(s, pattern)` that takes a string `s` and a regular expression pattern as input, and returns 'Valid' if the string matches the pattern, and 'Invalid' otherwise. The function should use regular expressions and not arrays or loops.
"""

import re

def validate_string(s, pattern):
    if re.match(pattern, s):
        return 'Valid'
    else:
        return 'Invalid'