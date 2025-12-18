"""
QUESTION:
Create a function called `extract_unique_words` that takes a string `disclaimer_text` as input. The function should return a sorted list of unique words present in the disclaimer, where a word is defined as a sequence of characters separated by spaces, punctuation marks, or line breaks. The function should be case-insensitive, considering "Word" and "word" as the same.
"""

import re

def extract_unique_words(disclaimer_text):
    # Convert the text to lowercase and use regular expression to find all words
    words = re.findall(r'\b\w+\b', disclaimer_text.lower())
    # Return the sorted list of unique words
    return sorted(list(set(words)))