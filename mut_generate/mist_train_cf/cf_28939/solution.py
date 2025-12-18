"""
QUESTION:
Implement a function `wordCount` that takes a string `s` as input, counts the occurrences of each unique word (a sequence of alphanumeric characters separated by spaces), and returns a dictionary containing the word counts. The function should ignore punctuation and treat uppercase and lowercase letters as equivalent. The word counts should be in descending order based on their frequency. The function should return the dictionary where keys are the unique words and values are the counts of each word.
"""

import re

def wordCount(s: str) -> dict:
    words = re.findall(r'\b\w+\b', s.lower())
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return dict(sorted(word_count.items(), key=lambda x: x[1], reverse=True))