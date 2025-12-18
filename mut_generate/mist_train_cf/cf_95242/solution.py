"""
QUESTION:
Given a paragraph of at most 10^6 characters, write a function `find_three_most_frequent_words(paragraph)` that returns the three most frequent words in the paragraph. The function should ignore all non-alphabetic characters, be case-insensitive, and return words with the same frequency in lexicographically ascending order. The solution should have a time complexity of O(n log n) and a space complexity of O(n), where n is the number of distinct words in the paragraph.
"""

import re

def find_three_most_frequent_words(paragraph):
    # Remove non-alphabetic characters and convert to lowercase
    paragraph = re.sub(r'[^a-zA-Z\s]', '', paragraph.lower())

    # Split the paragraph into individual words
    words = paragraph.split()

    # Count the frequency of each word
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    # Find the three most frequent words
    top_words = sorted(word_freq.keys(), key=lambda x: (-word_freq[x], x))[:3]

    return top_words