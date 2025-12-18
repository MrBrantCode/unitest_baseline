"""
QUESTION:
Write a Python function `filter_strings(lst, length)` that filters a list of strings `lst` and returns a list of strings with lengths greater than the given `length`. The function should ignore strings containing special characters (non-alphanumeric and non-underscore) and remove duplicates from the resulting list.
"""

import re

def filter_strings(lst, length):
    filtered_lst = []
    for string in lst:
        if len(string) > length and re.match("^[a-zA-Z0-9_]*$", string):
            filtered_lst.append(string)
    return list(set(filtered_lst))