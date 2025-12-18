"""
QUESTION:
Write a function `find_most_common_words` that takes a string as input and returns a list of the top three most common words, excluding common stop words and words shorter than three characters, along with their frequency counts, in descending order. The function should consider punctuation or special characters as word separators and ignore case differences.
"""

import re
from collections import Counter

def find_most_common_words(string):
    stop_words = {'the', 'a', 'an', 'and', 'etc.'}
    words = re.findall(r'\b\w+\b', string.lower())
    word_counter = Counter(words)
    
    for word in list(word_counter):
        if word in stop_words or len(word) < 3:
            del word_counter[word]
    
    most_common_words = word_counter.most_common(3)
    return most_common_words