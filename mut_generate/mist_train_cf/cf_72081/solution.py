"""
QUESTION:
Create a function named `split_string_to_words` that takes a string `text` as input and returns a list of words with more than 4 characters, ignoring common punctuation (".", ",", "!", "?"). The function should handle situations where punctuation is attached to the words.
"""

import string

def split_string_to_words(text):
    words = (word.strip(string.punctuation) for word in text.split())
    long_words = [word for word in words if len(word) > 4]
    return long_words