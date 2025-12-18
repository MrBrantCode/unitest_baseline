"""
QUESTION:
Write a function called `word_frequency` that takes a string of text as input and returns a list of tuples containing unique words and their frequencies, sorted in descending order by frequency. A word is defined as a sequence of alphanumeric characters separated by non-alphanumeric characters, and words should be converted to lowercase.
"""

import re
from collections import Counter

def word_frequency(text):
    # Convert text to lowercase and remove punctuation
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text.lower())
    # Split the text into words
    words = re.findall(r'\b\w+\b', text)
    # Count the frequency of each word
    word_counts = Counter(words)
    # Sort the word counts in descending order
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_word_counts