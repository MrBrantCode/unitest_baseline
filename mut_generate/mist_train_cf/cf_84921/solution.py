"""
QUESTION:
Create a function `check_string(s)` that identifies if a given string `s` contains a semi-colon (`;`) and does not contain any type of brackets (`()`, `[]`, `{}`). The string `s` can be of any length up to 500 characters, and may contain spaces and other symbols. The function should also be capable of identifying Greek question marks (;) and Arabic semi-colons (;) as semi-colons. The function should return `True` if the string meets the conditions and `False` otherwise.
"""

import re

def check_string(s):
    if len(s) > 500: 
        return False # edge case: string should be of max 500 length

    # checking if string contains semi-colon but without any type of brackets
    return bool(re.match(r'^[^()[\]{}]*;[^()[\]{}]*$', s))