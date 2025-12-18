"""
QUESTION:
Write a function named `is_valid_identifier` to check if a given string is a valid identifier in the C++ programming language. A valid identifier is a sequence of letters, digits, and underscores that does not start with a digit.
"""

import re

def is_valid_identifier(s):
    # In C++, a valid identifier is a sequence of letters, digits, and underscores 
    # that does not start with a digit.
    return re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', s) is not None