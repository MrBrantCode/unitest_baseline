"""
QUESTION:
Write a function `find_word_occurrences` that takes two parameters: `string` and `substring`. The function should return all occurrences of the complete word `substring` in the `string` in a case-insensitive manner, ignoring substrings within larger words. The function should have a time complexity of O(n), where n is the length of the string, and should consider a substring as a separate word if it is surrounded by whitespace or punctuation marks.
"""

import re

def find_word_occurrences(string, substring):
    pattern = r'\b{}\b'.format(substring)
    occurrences = re.findall(pattern, string, flags=re.IGNORECASE)
    return occurrences