"""
QUESTION:
Write a regex pattern to match all characters in a string that start with a lowercase letter. The pattern should match one or more characters, where the first character is lowercase and the following characters can be either uppercase or lowercase.
"""

import re

def entrance(s):
    pattern = r"[a-z][a-zA-Z]*"
    return re.findall(pattern, s)