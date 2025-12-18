"""
QUESTION:
Write a function `get_top_10_words(text)` that finds the top 10 most common words in a given string, excluding common stop words. The function should return a list of the top 10 words and have a time complexity of O(nlogn), where n is the length of the input string.
"""

import re
from collections import Counter

def get_top_10_words(text):
    stop_words = ['the', 'and', 'a', 'is', 'it', 'of', 'in', 'to', 'that', 'for']
    
    words = re.findall(r'\b\w+\b', text.lower())
    
    word_counts = Counter(word for word in words if word not in stop_words)
    
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    
    top_10_words = [word for word, count in sorted_words[:10]]
    
    return top_10_words