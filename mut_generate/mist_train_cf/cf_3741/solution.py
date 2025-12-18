"""
QUESTION:
Implement a function `most_frequent_words` that takes a paragraph as input and returns the five most frequent words. The words are case-insensitive, all non-alphabetic characters should be ignored, and words with the same frequency should be returned in lexicographically ascending order. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the number of distinct words in the paragraph.
"""

from collections import Counter
import re
import heapq

def most_frequent_words(paragraph):
    words = re.findall(r'\b\w+\b', paragraph.lower())
    word_count = Counter(words)
    return [word for word, _ in heapq.nsmallest(5, word_count.items(), key=lambda x: (-x[1], x[0]))]