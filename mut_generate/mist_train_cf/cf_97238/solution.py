"""
QUESTION:
Create a function named `get_most_frequent_words` that takes a string as input. The function should return a list of the 5 most frequent words in the string, excluding common English stop words and words with less than 4 characters. The function should handle cases and punctuation marks properly.
"""

import re
from collections import Counter

def get_most_frequent_words(string):
    # Create a list of stop words
    stop_words = ["the", "and", "a", "it", "is", "for", "in", "on", "of", "an", "am"]

    # Remove punctuation marks from the string
    string = re.sub(r'[^\w\s]', '', string)

    # Convert the string to lowercase
    string = string.lower()

    # Split the string into words
    words = string.split()

    # Remove stop words and words with less than 4 characters
    words = [word for word in words if word not in stop_words and len(word) >= 4]

    # Count the frequency of each word
    word_counts = Counter(words)

    # Get the 5 most frequent words
    most_frequent_words = word_counts.most_common(5)

    return most_frequent_words