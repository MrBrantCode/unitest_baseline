"""
QUESTION:
Write a function `count_pattern_occurrences` that takes two strings as input, `string` and `pattern`, and returns the number of times the `pattern` occurs in the `string`. The `pattern` can be any valid regular expression and the function should handle overlapping occurrences and special characters such as `*`, `+`, `?`, and nested patterns within the main pattern, as well as lookaheads and lookbehinds. The function should be case-sensitive.
"""

import re

def count_pattern_occurrences(string, pattern):
    count = 0
    regex = re.compile(pattern)
    matches = re.finditer(regex, string)
    for match in matches:
        count += 1
    return count