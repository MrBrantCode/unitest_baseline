"""
QUESTION:
Write a function `kth_most_frequent_word(s, k)` that takes a string `s` and an integer `k` as inputs, and returns the kth most frequent word with a length of at least 5 characters in the string. The words in the string should be treated as case-insensitive. If k is out of range, the function should return None.
"""

import re
from collections import Counter

def kth_most_frequent_word(s, k):
    words = re.findall(r'\b\w+\b', s)  
    words = [word.lower() for word in words if len(word) >= 5]  
    
    word_counts = Counter(words)
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    
    if k <= len(sorted_words):
        return sorted_words[k-1][0]  
    else:
        return None  