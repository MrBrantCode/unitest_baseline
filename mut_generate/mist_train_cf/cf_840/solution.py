"""
QUESTION:
Write a function `regex_match_all` that takes a string and a regular expression pattern as input, and returns all matches found at the beginning of the string. The function should have a time complexity of O(n), where n is the length of the input string. The function should ignore any matches that occur elsewhere in the string and return all matches, not just the first match.
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