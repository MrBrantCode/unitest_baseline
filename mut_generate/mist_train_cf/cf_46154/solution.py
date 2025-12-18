"""
QUESTION:
Create a function called `filter_out_non_alphanumeric` that takes a string input and extracts only alphanumeric characters. The function should ignore case sensitivity and discard any block of alphanumeric characters exceeding a length of 10.
"""

import re

def filter_out_non_alphanumeric(sentence):
    sentence_words = sentence.lower().split()
    filtered_words = [re.findall(r'\b\w{1,10}\b', word) for word in sentence_words]
    flattened_and_joined = ' '.join(sum(filtered_words, []))
    return flattened_and_joined