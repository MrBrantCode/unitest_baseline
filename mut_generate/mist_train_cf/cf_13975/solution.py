"""
QUESTION:
Write a function `find_kth_most_frequent_word(s, k)` that takes a string `s` and an integer `k` as input and returns the kth most frequent word with a length of at least 5 characters in the string, ignoring case. If k is greater than the number of unique words with a length of at least 5 characters, the function should return `None`.
"""

import re
from collections import Counter

def find_kth_most_frequent_word(s, k):
    words = re.findall(r'\b\w{5,}\b', s.lower())
    word_counts = Counter(words)
    sorted_words = sorted(word_counts, key=lambda x: word_counts[x], reverse=True)
    return sorted_words[k-1] if k <= len(sorted_words) else None