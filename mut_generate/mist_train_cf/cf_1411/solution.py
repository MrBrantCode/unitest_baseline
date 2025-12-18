"""
QUESTION:
Create a function named `count_unique_words` that takes a sentence as input and returns a list of tuples containing unique words (excluding common stopwords) and their frequency counts in descending order. The function should be able to handle sentences with up to 100 million characters, punctuation marks, special characters, and emojis, and should have a time complexity of O(n), where n is the length of the sentence. The function should also be case-insensitive.
"""

import re
import string
from collections import Counter

def count_unique_words(sentence):
    # Define a list of common stopwords
    stopwords = ['a', 'an', 'the', 'is', 'are', 'and', 'or', 'in', 'on', 'at', 'to', 'for']

    # Remove punctuation marks and special characters
    sentence = re.sub(r'[^\w\s]', '', sentence)

    # Convert the sentence to lowercase
    sentence = sentence.lower()

    # Split the sentence into words
    words = sentence.split()

    # Remove stopwords from the list of words
    words = [word for word in words if word not in stopwords]

    # Count the frequency of each unique word
    word_counts = Counter(words)

    # Sort the word counts in descending order
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    return sorted_word_counts