"""
QUESTION:
Implement a function `split_string` that takes two parameters: `my_string` and `delimiter`. Split `my_string` into a list of substrings according to `delimiter`, where `delimiter` can be a single character or a regular expression.
"""

import re

def split_string(my_string, delimiter):
    if len(delimiter) == 1:
        return my_string.split(delimiter)
    else:
        return re.split(delimiter, my_string)