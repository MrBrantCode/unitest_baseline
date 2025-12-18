"""
QUESTION:
Create a function named `count_unique_words` that takes a string `text` as input and returns the number of unique words in the text. The function should handle punctuation marks, numbers, and special characters, and it should be case-insensitive. The time complexity should be O(n), where n is the length of the text, and the space complexity should be O(m), where m is the number of unique words in the text.
"""

import re

def count_unique_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    unique_words = set(words)
    return len(unique_words)