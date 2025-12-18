"""
QUESTION:
Implement the `test_corpus` function which takes a function `get_text_from_file` that returns the text content of a file as a string. The function should read the text content from the file using `get_text_from_file`, convert the text to lowercase, tokenize the text into individual words (removing punctuation and non-alphabetic characters), count the frequency of each word, and return a dictionary with unique words as keys (in lowercase) and their frequencies as values.
"""

import re
from collections import defaultdict

def get_word_frequencies(get_text_from_file):
    text = get_text_from_file().lower()
    words = re.findall(r'\b\w+\b', text)
    word_freq = defaultdict(int)
    for word in words:
        word_freq[word.lower()] += 1
    return dict(word_freq)