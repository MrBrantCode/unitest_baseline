"""
QUESTION:
Write a function `get_top_10_words(text)` that takes a string as input, returns a list of the top 10 most common words in the string, excluding common stop words, and has a time complexity of O(nlogn), where n is the length of the input string. The function should ignore case and only consider alphanumeric words.
"""

import re
from collections import Counter

def get_top_10_words(text):
    stop_words = ['the', 'and', 'a', 'is', 'it', 'of', 'in', 'to', 'that', 'for']
    
    # Convert text to lowercase and split into individual words
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Count the occurrence of each word (excluding stop words)
    word_counts = Counter(word for word in words if word not in stop_words)
    
    # Sort the dictionary by the count of each word in descending order
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Take the top 10 words
    top_10_words = [word for word, count in sorted_words[:10]]
    
    return top_10_words