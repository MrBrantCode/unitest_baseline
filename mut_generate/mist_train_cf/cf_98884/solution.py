"""
QUESTION:
Write a function named `clean_sentence` that takes an input sentence as a string, removes any punctuation at the end of the sentence, and returns the cleaned sentence. The function should handle sentences ending with question marks, exclamation marks, periods, or no punctuation at all.
"""

import re

def clean_sentence(sentence):
    # Remove any punctuation at the end of the sentence
    cleaned_sentence = re.sub(r'[.?!]+$', '', sentence)
    return cleaned_sentence