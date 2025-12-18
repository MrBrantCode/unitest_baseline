"""
QUESTION:
Write a function `reverse_words_k_length(s, k)` to reverse all the words with length `k` in a given string `s` while preserving the original case and punctuation. The function should be case-insensitive and handle punctuation correctly, leaving it on the same side of the word after reversal.
"""

import re

def reverse_words_k_length(s, k):
    words = re.findall(r'\b\w+\b', s, re.I)
    for word in words:
        if len(word) == k:
            pattern = re.compile(re.escape(word), re.I)
            s = pattern.sub(lambda m: m.group(0)[::-1], s)
    return s