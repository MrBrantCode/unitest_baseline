"""
QUESTION:
Implement a function `convert_string_to_list` that takes a string as input. The function should remove all punctuation marks, numbers, and special characters from the string, then split the cleaned string into a list of words, remove any duplicate words, and sort the list in alphabetical order.
"""

import re

def convert_string_to_list(string):
    cleaned_string = re.sub(r'[^a-zA-Z\s]', '', string)
    words = cleaned_string.split()
    unique_words = list(set(words))
    sorted_words = sorted(unique_words)
    return sorted_words