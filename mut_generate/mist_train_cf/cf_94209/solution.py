"""
QUESTION:
Write a function named `count_unique_words` that takes a sentence as input and returns the number of unique words in the sentence, excluding common stopwords. The function should handle sentences containing punctuation marks, special characters, and emojis. It should have a time complexity of O(n), where n is the length of the sentence. The sentence can have up to 10 million characters.
"""

import re
from collections import Counter

def count_unique_words(sentence):
    # Define common stopwords
    stopwords = set(['the', 'a', 'an', 'in', 'on', 'is', 'are', 'was', 'were', 'to', 'for', 'of', 'and', 'or', 'with'])

    # Remove punctuation marks and special characters
    sentence = re.sub(r'[^\w\s]', '', sentence)

    # Split sentence into words and convert to lowercase
    words = sentence.lower().split()

    # Remove stopwords and emojis
    words = [word for word in words if word not in stopwords and not any(not char.isalpha() for char in word)]

    # Count unique words
    word_counts = Counter(words)
    unique_word_count = len(word_counts)

    return unique_word_count