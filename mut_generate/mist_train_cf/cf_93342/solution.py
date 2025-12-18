"""
QUESTION:
Create a function called `get_most_frequent_words(text, n)` that takes a string `text` and an integer `n` as input, and returns the `n` most frequent words in the string. The function should exclude common English stop words, handle cases and punctuation marks properly, and return the result as a list of tuples where each tuple contains a word and its frequency.
"""

import re
from collections import Counter

def get_most_frequent_words(text, n):
    # Define a list of common English stop words
    stop_words = ["the", "and", "a", "is", "it", "for", "of", "in", "on", "are", "am", "to"]

    # Convert the string to lowercase and remove punctuation marks
    cleaned_text = re.sub(r'[^\w\s]', '', text.lower())

    # Split the cleaned text into words
    words = cleaned_text.split()

    # Exclude stop words from the list of words
    words = [word for word in words if word not in stop_words]

    # Count the frequency of each word
    word_counts = Counter(words)

    # Get the n most frequent words
    most_frequent_words = word_counts.most_common(n)

    return most_frequent_words