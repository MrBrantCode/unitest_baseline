"""
QUESTION:
Write a function called `find_most_common_words` that takes a string as input and returns a list of the top three most common words, along with their frequency counts, in descending order. The function should exclude any common stop words such as "the", "a", "an", "and", etc., handle cases where words are separated by punctuation marks or special characters, and ignore any words that are shorter than three characters.
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