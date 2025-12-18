"""
QUESTION:
Create a function `process_text(text)` that takes a string as input, converts it to uppercase, removes all numeric characters and special characters except exclamation marks (!) and apostrophes ('), splits the text into words, and returns a dictionary-like object with the word count for each unique word.
"""

import re
from collections import Counter

def process_text(text):
    # convert the text to uppercase
    upper_text = text.upper()

    # removes all numeric characters and special characters except exclamation marks(!) and apostrophes(')
    updated_text = re.sub(r"[^A-Z !']+", '', upper_text)

    # split the text into words
    words = updated_text.split()

    # count the occurrence of each word
    word_count = Counter(words)

    return word_count