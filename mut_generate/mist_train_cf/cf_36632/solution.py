"""
QUESTION:
Write a function `remove_commented_lines` that takes a string `s` as input and returns the modified string with all lines starting with "//" removed. The input string may contain multiple lines and the commented lines may be anywhere in the string.
"""

import re

def remove_commented_lines(s):
    return re.sub(pattern='//.*\n?', repl='', string=s)