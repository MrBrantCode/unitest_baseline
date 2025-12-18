"""
QUESTION:
Construct a regex pattern for a function named `match_words` that matches the given list of words exactly. The function should have a time complexity of O(n), where n is the number of words in the list. The function should not match any other words outside the given list.
"""

import re

def match_words(words):
    pattern = "^(" + "|".join(words) + ")$"
    return re.compile(pattern)