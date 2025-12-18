"""
QUESTION:
Write a function named `mostCommonWord` that takes two parameters: `paragraph` and `banned`. `paragraph` is a string that may contain English letters, spaces, and certain punctuation marks (!?',;.). The function should return the most common word in `paragraph` that is not in the `banned` array. The function should be case-insensitive and disregard punctuation. The length of `paragraph` is between 1 and 1000 characters, and the length of `banned` is between 0 and 100. Each string in `banned` is between 1 and 10 characters long and contains only lowercase English letters.
"""

import re
from collections import defaultdict

def mostCommonWord(paragraph, banned):
    banned_words = set(banned)
    words = re.findall(r'\w+', paragraph.lower())
    word_count = defaultdict(int)
    for word in words:
        if word not in banned_words:
            word_count[word] += 1
    return max(word_count, key = word_count.get)