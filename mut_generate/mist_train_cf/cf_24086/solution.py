"""
QUESTION:
Write a function `no_cat_regex` that generates a regular expression pattern that matches any string that does not contain the substring "cat".
"""

import re

def no_cat_regex(s):
    pattern = re.compile(r'^(?:(?!cat).)*$')
    return bool(pattern.match(s))