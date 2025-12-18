"""
QUESTION:
Write a Python function called `clean_sentence` that takes a sentence as input and returns the sentence with any punctuation at the end removed. The function should handle sentences ending with question marks, exclamation marks, periods, or no punctuation at all. The function should use regular expressions to achieve this.
"""

import re
def clean_sentence(sentence):
    cleaned_sentence = re.sub(r'[.?!]+$', '', sentence)
    return cleaned_sentence