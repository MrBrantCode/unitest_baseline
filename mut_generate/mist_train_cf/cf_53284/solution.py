"""
QUESTION:
Write a function `replace_whitespace_with_comma` that takes a string as input and returns the modified string where all occurrences of one or more alphabetical characters followed by one or more whitespace characters (tabs and/or spaces) followed by one or more numerical characters followed by a semicolon are replaced with the alphabetical characters followed by a comma followed by the numerical digits and then the semicolon.
"""

import re

def replace_whitespace_with_comma(s):
    return re.sub(r"([a-zA-Z]+)(\s+)(\d+)(;)", r'\1,\3;', s)