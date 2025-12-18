"""
QUESTION:
Implement a function `find_three_most_frequent_words(paragraph)` that finds the three most frequent words in a given paragraph. The function should ignore non-alphabetic characters, consider words as case-insensitive, and return words with the same frequency in lexicographically ascending order. The function should have a space complexity of O(n), where n is the number of distinct words in the paragraph.
"""

import re
from collections import Counter

def find_three_most_frequent_words(paragraph):
    # Step 1: Remove non-alphabetic characters and convert to lowercase
    paragraph = re.sub(r'[^a-zA-Z\s]', '', paragraph.lower())

    # Step 2: Split the paragraph into individual words
    words = paragraph.split()

    # Step 3 & 4: Count the frequency of each word and find the three most frequent words
    word_freq = Counter(words)
    top_words = sorted(word_freq, key=lambda x: (-word_freq[x], x))[:3]

    return top_words