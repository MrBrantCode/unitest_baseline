"""
QUESTION:
Implement a function `split_string(my_string, delimiter)` that takes a string `my_string` and a delimiter as input. The delimiter can be one or more characters long and can also be a regular expression. Split the input string according to the given delimiter and return the resulting list of substrings.
"""

import re

def split_string(my_string, delimiter):
    if len(delimiter) == 1:
        return my_string.split(delimiter)
    else:
        return re.split(delimiter, my_string)