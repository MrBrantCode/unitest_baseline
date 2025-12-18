"""
QUESTION:
Create a function named `probe_word_group_frequency` that takes two string parameters, `phrase1` and `phrase2`, and returns a boolean value indicating whether the two phrases contain the exact same set of words with identical frequency, regardless of word order. The function should consider words as case-insensitive and ignore non-word characters.
"""

from collections import Counter
import re

def probe_word_group_frequency(phrase1: str, phrase2: str):
    words1 = re.findall(r'\b\w+\b', phrase1.lower())
    words2 = re.findall(r'\b\w+\b', phrase2.lower())
    
    ctr1 = Counter(words1)
    ctr2 = Counter(words2)
    
    return ctr1 == ctr2