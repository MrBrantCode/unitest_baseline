"""
QUESTION:
Write a function named `break_down_text` that takes a string `text` as input and returns a list of unique words in the text, ignoring punctuation marks and considering word case insensitive. The function should have a time complexity of O(n), where n is the length of the text.
"""

import string

def break_down_text(text):
    # Remove punctuation marks
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Split text into individual words
    words = text.split()

    # Convert words to lowercase
    words = [word.lower() for word in words]

    # Remove duplicates by converting list to set and then back to list
    words = list(set(words))

    return words