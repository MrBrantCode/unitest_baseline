"""
QUESTION:
Write a function `count_pattern_occurrences` that takes two parameters, `string` and `pattern`, and returns the number of times the `pattern` appears in the `string` as a whole word, considering the following conditions: the pattern can be surrounded by any number of whitespace characters, punctuation marks, digits, or non-alphanumeric characters (excluding whitespace and punctuation marks). The pattern should not be part of another word and the search should be case-sensitive.
"""

import re

def count_pattern_occurrences(string, pattern):
    regex_pattern = r"(?<!\w){}(?!\w)".format(re.escape(pattern))
    matches = re.findall(regex_pattern, string)
    return len(matches)