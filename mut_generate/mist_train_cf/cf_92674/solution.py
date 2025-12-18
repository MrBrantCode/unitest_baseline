"""
QUESTION:
Implement a function named `break_down_text` that takes a string of text as input, ignores punctuation marks, and returns a list of unique words in the text. The function should have a time complexity of O(n), where n is the length of the text.
"""

import string

def break_down_text(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    words = [word.lower() for word in words]
    words = list(set(words))
    return words