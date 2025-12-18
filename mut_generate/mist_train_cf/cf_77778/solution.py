"""
QUESTION:
Develop a function named `pattern_matcher` that takes a string `text` as input and returns all occurrences of the words "start", "end", and "here" in the string, regardless of their case and whether they are followed by punctuation. The function should consider these words as whole words only, not as part of other words, and should return them in the case they appear in the original string.
"""

import re

def pattern_matcher(text):
    pattern = re.compile(r'\b(start|end|here)\b\W?', re.IGNORECASE)
    matches = pattern.findall(text)
    return matches