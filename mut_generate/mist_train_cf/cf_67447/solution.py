"""
QUESTION:
Write a function `remove_consecutive_whitespaces` that takes a string `s` as input and returns a new string where all consecutive occurrences of any whitespace characters (\t, \n, \r, \f, \v, space) are replaced with a single space. The function should be optimized for handling large strings and should not exceed the maximum recursion depth. If all types of whitespace characters are to be treated as the same and replaced with a single space, consider using a regular expression approach.
"""

import re

def remove_consecutive_whitespaces(s):
    return re.sub(r'\s+', ' ', s)