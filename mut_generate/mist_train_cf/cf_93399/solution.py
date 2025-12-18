"""
QUESTION:
Write a function `count_word_occurrences(string, word)` that takes a string and a word as input and returns the number of occurrences of the word in the string. The function should perform a case-insensitive search and only consider complete word matches, ignoring substrings within larger words.
"""

import re

def count_word_occurrences(string, word):
    pattern = r'\b{}\b'.format(word)  # construct a regex pattern for whole word match
    matches = re.findall(pattern, string, re.IGNORECASE)  # find all matches using regex
    return len(matches)  # return the count of matches