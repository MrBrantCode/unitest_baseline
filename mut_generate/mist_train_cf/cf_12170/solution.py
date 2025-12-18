"""
QUESTION:
Write a function that uses a regular expression to match all strings starting with a lowercase 'a', followed by any number of lowercase letters, and ending with an uppercase 'Z'.
"""

import re

def entrance(s):
    pattern = r'^a[a-z]*Z$'
    return bool(re.match(pattern, s))