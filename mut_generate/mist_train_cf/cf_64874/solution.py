"""
QUESTION:
Create a function named `get_most_frequent_word` that takes a string of characters as input. The function should ignore prevalent English filler words such as "the", "is", "in", "and", "of", "a", "an", "to", "as", and "for", and return the word that appears most frequently in the input string, regardless of case. The input string may contain punctuation and words may be separated by spaces or commas.
"""

import re
from collections import Counter

def get_most_frequent_word(text):
    # List of English filler words
    filler_words = ['the', 'is', 'in', 'and', 'of', 'a', 'an', 'to', 'as', 'for']

    # Remove punctuation and make all lower case
    text = re.sub(r'[^\w\s]', '', text.lower())

    # Split text into list of words and filter out any filler words
    words = [word for word in text.split() if word not in filler_words]

    # Count frequency of each word
    word_counts = Counter(words)

    # Get the most frequent word
    most_frequent_word = word_counts.most_common(1)[0][0]

    return most_frequent_word