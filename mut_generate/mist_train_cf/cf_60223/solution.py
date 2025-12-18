"""
QUESTION:
Create a function `predict_word(input_text, list_of_words, n=3)` that takes an input string `input_text` and a list of words `list_of_words`, and returns a list of up to `n` words from `list_of_words` that closely match `input_text` based on a similarity metric. The function should ignore case differences between the input text and the words in the list.
"""

import difflib

def predict_word(input_text, list_of_words, n=3):
    close_matches = difflib.get_close_matches(input_text.lower(), list_of_words, n=n)
    return close_matches