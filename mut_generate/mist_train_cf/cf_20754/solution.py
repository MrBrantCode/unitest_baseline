"""
QUESTION:
Write a function `count_unique_words(text)` that estimates the number of unique words in a given text, handling punctuation marks, numbers, and special characters efficiently. The function should have a time complexity of O(n), where n is the length of the text, and a space complexity of O(m), where m is the number of unique words in the text.
"""

import re

def count_unique_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    unique_words = set(words)
    return len(unique_words)