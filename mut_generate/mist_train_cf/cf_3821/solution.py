"""
QUESTION:
Write a Python function named `count_unique_words` that takes a string `paragraph` as input, ignores case sensitivity, and returns the count of unique words that are at least 3 characters long and do not contain special characters or numbers, excluding common English words like 'the', 'and', 'or', etc.
"""

import re

def count_unique_words(paragraph):
    paragraph = paragraph.lower()
    paragraph = re.sub(r'[^a-zA-Z\s]', '', paragraph)
    common_words = ['the', 'and', 'or', 'like']
    words = paragraph.split()
    words = [word for word in words if len(word) >= 3 and word not in common_words]
    unique_words = set(words)
    return len(unique_words)