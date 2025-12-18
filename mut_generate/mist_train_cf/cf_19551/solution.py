"""
QUESTION:
Create a function `count_occurrences` that takes two strings `string1` and `string2` as input. The function should return the number of times `string1` is found within `string2`, considering a case-insensitive search. The search should only count matches that are surrounded by spaces or punctuation marks. If `string2` is empty, return -1. If `string1` is empty, return 0.
"""

import re

def count_occurrences(string1, string2):
    if string2 == "":
        return -1

    if string1 == "":
        return 0

    pattern = r"(?<![^\W_])" + re.escape(string1) + r"(?![^\W_])"
    matches = re.findall(pattern, string2, re.IGNORECASE)
    return len(matches)