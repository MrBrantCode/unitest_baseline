"""
QUESTION:
Create a function `match_string(s)` that takes a string `s` as input and returns `True` if the string contains a semi-colon `";"`, followed by zero or more spaces, and does not contain any alphabetical characters after the semi-colon, and `False` otherwise.
"""

import re

def match_string(s):
    pattern = r'^.*;[ ]*[^a-zA-Z]*$'
    if re.match(pattern, s):
        return True
    else:
        return False