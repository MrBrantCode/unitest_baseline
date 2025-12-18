"""
QUESTION:
Implement a function named `process_string(s)` that takes a string `s` as input. The function should convert the string to lowercase, remove all punctuation, split the string into a list of words, and return a list of unique words that appear only once in the string.
"""

import re
from collections import Counter

def process_string(s):
    # Remove punctuation and convert to lowercase
    s = re.sub(r'[^\w\s]', '', s).lower()

    # Split into words
    words = s.split()

    # Count word frequencies
    word_count = Counter(words)

    # Only keep words that appear once
    return [word for word in word_count if word_count[word] == 1]