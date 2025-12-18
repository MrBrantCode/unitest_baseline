"""
QUESTION:
Write a function `count_words(text)` that takes a string of text as input, counts the occurrences of each word in the text, and returns or prints the top 5 most frequently used words, ignoring case and punctuation. The words should be counted in a case-insensitive manner and all non-alphanumeric characters except spaces should be ignored.
"""

from collections import Counter
import re

def count_words(text):
    # Remove punctuation and convert text to lowercase
    text = re.sub(r'[^\w\s]', '', text.lower())

    # Count the occurrences of each word
    word_counts = Counter(text.split())

    # Return the top 5 most frequently used words
    return word_counts.most_common(5)