"""
QUESTION:
Write a function `match_start_end` that takes two characters, `start` and `end`, as input and returns a regular expression pattern that matches any string that starts with `start` and ends with `end`. The function should return a regex pattern as a string.
"""

import re

def match_start_end(start, end):
    return '^' + re.escape(start) + '.*' + re.escape(end) + '$'