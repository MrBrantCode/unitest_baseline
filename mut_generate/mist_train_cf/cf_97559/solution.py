"""
QUESTION:
Create a function called `clean_sentence` that takes a sentence as input and returns the sentence with any punctuation at the end removed. The function should handle sentences with question marks, exclamation marks, periods, or no punctuation at all.
"""

import re

def clean_sentence(sentence):
    # Remove any punctuation at the end of the sentence
    cleaned_sentence = re.sub(r'[.?!]+$', '', sentence)
    return cleaned_sentence