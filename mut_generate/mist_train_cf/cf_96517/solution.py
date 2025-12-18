"""
QUESTION:
Write a function `count_words` that takes a string `text` as input, returns a dictionary where keys are unique words in the string and values are the corresponding word frequencies. The function should be case-insensitive and ignore special characters. Optimize the function for space complexity.
"""

import re

def count_words(text):
    word_counts = {}
    words = re.findall(r'\w+', text.lower())
    
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    return word_counts