"""
QUESTION:
Create a function `word_count` that takes a string as input and returns a dictionary. The dictionary should contain each word from the string as a key and its count as the value. The function should ignore common stopwords and words with less than 3 characters. The input string may contain punctuation marks, different casing, and multiple whitespace characters. The returned dictionary should be sorted in descending order based on the word counts. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the length of the input string.
"""

import re
from collections import Counter

def word_count(string):
    # Define the common stopwords
    stopwords = {'the', 'and', 'is', 'a', 'an', 'in', 'of', 'to', 'that', 'it', 'for', 'on', 'with', 'as', 'at', 'by', 'from', 'are', 'was', 'were', 'be', 'or'}

    # Preprocess the string: remove punctuation, convert to lowercase, and split into words
    words = re.findall(r'\b\w+\b', string.lower())

    # Count the words, ignoring stopwords and words with less than 3 characters
    word_counts = Counter(word for word in words if len(word) >= 3 and word not in stopwords)

    # Sort the word counts in descending order
    sorted_word_counts = dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True))

    return sorted_word_counts