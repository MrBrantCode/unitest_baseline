"""
QUESTION:
Create a function `find_word_matches(string, word)` that finds all occurrences of the word in a given string. The function should perform a case-insensitive search and only consider complete word matches. It should also be efficient for large strings with a time complexity of O(n), where n is the length of the string.
"""

import re

def find_word_matches(string, word):
    pattern = r'\b{}\b'.format(re.escape(word))
    matches = re.findall(pattern, string, flags=re.IGNORECASE)
    return matches