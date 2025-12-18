"""
QUESTION:
Implement the `_quote_if_contains` function. It should take two parameters, `value` and `pattern`, where `value` is the string to be quoted if it contains a matching character and `pattern` is a regular expression pattern to match against `value`. The function should return the quoted `value` if it contains any character matching the given `pattern`, and return the original `value` if no match is found.
"""

import re

def _quote_if_contains(value, pattern):
    if re.search(pattern, value):
        return f'"{value}"'
    return value