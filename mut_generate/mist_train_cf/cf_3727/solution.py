"""
QUESTION:
Write a function `word_count` that takes a list of sentences as input and returns a dictionary with unique alphabetic words as keys and their total occurrence counts as values. The function should be case-insensitive, exclude words containing only digits, ignore repeated words within each sentence, and disregard punctuation marks.
"""

import re
from collections import defaultdict

def word_count(sentences):
    word_dict = defaultdict(int)
    
    for sentence in sentences:
        words = re.findall(r'\b[a-zA-Z]+\b', sentence.lower())
        unique_words = set(words)
        for word in unique_words:
            word_dict[word] += 1
    
    return dict(word_dict)