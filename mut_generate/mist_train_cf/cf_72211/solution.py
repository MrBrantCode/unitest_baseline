"""
QUESTION:
Write a Python function called `punctuation_counter` that takes a string `text` as input and returns a dictionary containing the count of each type of punctuation mark in the text. The function should be able to handle all punctuation characters, including but not limited to period (.), comma (,), question mark (?), exclamation point (!), colon (:), semicolon (;), apostrophe ('), parentheses, and quotations.
"""

import collections
import string

def punctuation_counter(text):
    punctuation_chars = string.punctuation
    text_punctuation = [char for char in text if char in punctuation_chars]
    return dict(collections.Counter(text_punctuation))