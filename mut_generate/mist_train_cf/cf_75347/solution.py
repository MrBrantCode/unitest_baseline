"""
QUESTION:
Create a function `extract_unique_words(text)` that takes a string `text` as input, extracts unique words from it while ignoring punctuation marks, and returns them as a set. The function should treat the same word with different cases as the same word, and it should not include any punctuation marks in the output.
"""

import string

def extract_unique_words(text):
    # Remove punctuation from the text
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Convert to lower case to avoid duplicates of the same word with different cases
    text = text.lower()
    # Split the text into words and store them in a set to remove duplicates
    words = set(text.split())
    return words