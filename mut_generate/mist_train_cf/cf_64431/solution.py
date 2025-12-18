"""
QUESTION:
Write a function `most_frequent_non_stop_word` that takes a string `text` as input and returns the most frequent word in the string excluding a set of common English stop words. The function should consider words case-insensitively and ignore punctuation except for apostrophes.
"""

import collections
import string

def most_frequent_non_stop_word(text):
    # List of common English stop words
    stop_words = {'the', 'is', 'in', 'a', 'an', 'and', 'as', 'at', 'by', 'for', 'from', 'of', 'on', 'to', 'with', 'it', 'this'}

    # Remove punctuation except apostrophe, convert to lower case and split into words
    words = text.translate(str.maketrans('', '', string.punctuation.replace("'", ''))).lower().split()

    # Exclude stop words and count frequency of remaining words
    counter = collections.Counter(word for word in words if word not in stop_words)

    # Return the most common non-stop word
    return counter.most_common(1)[0]