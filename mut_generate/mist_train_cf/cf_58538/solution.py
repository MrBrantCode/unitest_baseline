"""
QUESTION:
Write a function `test_string` that uses a regex pattern to identify strings consisting exclusively of non-digit characters. The function should take a string `s` as input, match it against the regex pattern, and return whether the string matches the pattern. The regex pattern should capture any possible character other than numerical values (0-9) from the start to the end of the string.
"""

import re

def test_string(s):
    pattern = "^[^0-9]*$"
    return bool(re.match(pattern, s))