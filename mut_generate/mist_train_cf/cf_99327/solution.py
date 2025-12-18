"""
QUESTION:
Write a function `most_frequent_word` that takes a string `text` as input and returns the most frequent word in the text. The function should be case-insensitive and consider punctuation as word separators. The input text may contain multiple words with the same maximum frequency, in which case the function should return any of them.
"""

import re
from collections import Counter

def most_frequent_word(text: str) -> str:
    words = re.findall(r'\b\w+\b', text.lower())
    word_count = Counter(words)
    return word_count.most_common(1)[0][0]