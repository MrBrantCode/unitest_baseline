"""
QUESTION:
Create a function called `separate_words_and_punctuation` that takes a string of sentences as input and returns a list of words and punctuation as separate elements. The list should preserve the original order of words and punctuation, and punctuation should be treated as individual elements.
"""

import re

def separate_words_and_punctuation(sentences):
    return re.findall(r'\b\w+\b|\S', sentences)