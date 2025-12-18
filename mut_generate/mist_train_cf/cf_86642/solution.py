"""
QUESTION:
Write a function called `regex_match_all` that takes two parameters: `string` and `pattern`. The function should return a list of all occurrences of the pattern found at the beginning of the string, ignoring any matches that occur elsewhere in the string. The function should have a time complexity of O(n), where n is the length of the input string.
"""

import re

def regex_match_all(string, pattern):
    regex = re.compile('^' + pattern)
    matches = []
    index = 0
    while index < len(string):
        match = regex.match(string[index:])
        if match:
            matches.append(match.group())
            index += len(match.group())
        else:
            break
    return matches