"""
QUESTION:
Create a function named `count_lexical_items` that takes a string `text` as input, removes punctuation, converts the text to lowercase, and returns a dictionary where the keys are unique words and the values represent their frequency.
"""

import re
from collections import Counter

def count_lexical_items(text):
    # Clean text and split into a list
    words = re.sub(r'[^\w\s]','',text).lower().split()

    # Count unique words
    word_counts = Counter(words)
    return word_counts