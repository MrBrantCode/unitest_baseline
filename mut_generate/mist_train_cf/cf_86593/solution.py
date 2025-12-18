"""
QUESTION:
Design a function `count_pattern_occurrences` that takes two parameters, `string` and `pattern`, and returns the count of occurrences of the pattern in the string. The pattern can be any regular expression, including patterns with special characters, nested patterns, lookaheads, and lookbehinds. The function should handle overlapping occurrences of the pattern in the string.
"""

import re

def count_pattern_occurrences(string, pattern):
    count = 0
    regex = re.compile(pattern)
    matches = re.finditer(regex, string)
    for match in matches:
        count += 1
    return count