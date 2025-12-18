"""
QUESTION:
Write a function `word_count(s)` that takes a string `s` as input, counts the number of unique words in the string, and returns the frequency of each word. The function should treat words with case variations as the same word, and words separated by hyphens should be treated as a single word. Punctuation and white spaces should be treated as word separators.
"""

import re
from collections import Counter

def word_count(s):
    s = s.lower()
    s = re.sub(r'[-]', '', s)
    s = re.sub(r'[^\w\s]', ' ', s)
    words = s.split()
    word_counts = Counter(words)
    unique_words = len(word_counts)
    return unique_words, word_counts