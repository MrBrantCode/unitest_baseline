"""
QUESTION:
Write a function `count_word_occurrences` that takes two parameters, `string` and `word`, and returns the number of occurrences of `word` in `string` as a whole word, regardless of case. The function should use regular expressions to ensure whole word matching.
"""

import re

def count_word_occurrences(string, word):
    pattern = r'\b{}\b'.format(word)  # construct a regex pattern for whole word match
    matches = re.findall(pattern, string, re.IGNORECASE)  # find all matches using regex
    return len(matches)  # return the count of matches