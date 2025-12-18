"""
QUESTION:
Create a function called `clean_sentence` that takes an input sentence and returns the sentence with any punctuation at the end removed. The function should handle varying punctuation marks, including question marks, exclamation marks, and periods.
"""

import re
def clean_sentence(sentence):
    # Remove any punctuation at the end of the sentence
    cleaned_sentence = re.sub(r'[.?!]+$', '', sentence)
    return cleaned_sentence