"""
QUESTION:
Write a function named `count_pattern_occurrences` that takes a string and a pattern as input, and returns the number of times the pattern occurs in the string as a whole word. The pattern can contain special characters, is case-sensitive, and should be counted if it appears surrounded by any number of whitespace characters, punctuation marks, digits, or non-alphanumeric characters (excluding whitespace and punctuation marks), but not as a substring within another word.
"""

import re

def count_pattern_occurrences(string, pattern):
    regex_pattern = r"(?<!\w){}(?!\w)".format(re.escape(pattern))
    matches = re.findall(regex_pattern, string)
    return len(matches)