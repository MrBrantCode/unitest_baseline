"""
QUESTION:
Construct a regex pattern for a function named `match_words` that matches exactly the words "cat", "bat", "rat", "mat", and "hat", while excluding any other words.
"""

import re

def match_words(word):
    pattern = r'\b(cat|bat|rat|mat|hat)\b'
    return bool(re.fullmatch(pattern, word))