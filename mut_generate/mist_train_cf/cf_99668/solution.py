"""
QUESTION:
Write a function `clean_sentence(sentence)` that takes a string `sentence` as input, removes any punctuation at the end of the sentence, and returns the cleaned sentence. The function should handle input sentences with varying punctuation, including question marks, exclamation marks, or no punctuation at all.
"""

import re

def clean_sentence(sentence):
    cleaned_sentence = re.sub(r'[.?!]+$', '', sentence)
    return cleaned_sentence