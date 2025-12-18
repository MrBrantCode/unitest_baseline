"""
QUESTION:
Write a function `regex_match(regex, string)` that performs regex matches on a given string and returns all matches found at the beginning of the string. The function should ignore any matches that occur elsewhere in the string.
"""

import re

def regex_match(regex, string):
    matches = []
    pattern = re.compile(regex)
    for match in pattern.finditer(string):
        if match.start() == 0:
            matches.append(match.group())
    return matches