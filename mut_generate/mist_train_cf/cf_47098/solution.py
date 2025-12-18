"""
QUESTION:
Write a regular expression function `pattern` that matches sentences containing the word "dog" followed by any number of characters except "x" and "y". The function should treat "dog" as a whole word, excluding permutations like "god" or "adogb".
"""

import re

def pattern(sentence):
    return bool(re.search(r'\bdog[^xy]*\b', sentence))