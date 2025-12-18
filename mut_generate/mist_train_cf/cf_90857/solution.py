"""
QUESTION:
Write a function `count_occurrences(text)` that takes a string `text` as input, counts the occurrences of the word "love" ignoring case sensitivity and only considering it as a standalone word, and returns the count. The function should handle cases where the word "love" appears multiple times in a single word.
"""

import re

def count_occurrences(text):
    count = 0
    pattern = r'\blove\b'
    matches = re.findall(pattern, text, flags=re.IGNORECASE)
    for match in matches:
        count += len(re.findall(r'love', match, flags=re.IGNORECASE))
    return count