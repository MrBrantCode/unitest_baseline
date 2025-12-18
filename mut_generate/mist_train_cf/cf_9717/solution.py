"""
QUESTION:
Create a function named `convert_string_to_word_list` that takes a string `s` as input, splits it into words, removes any punctuation marks or special characters, and returns a list of words sorted alphabetically while maintaining the original order of words with the same alphabetic order. The function should consider an apostrophe as part of a word and return an empty list if the input string is empty.
"""

import re

def convert_string_to_word_list(s):
    # Check if the string is empty
    if not s:
        return []

    # Use regular expressions to split the string into words
    words = re.findall(r"\w+(?:'\w+)?", s)

    # Sort the words alphabetically
    sorted_words = sorted(words)

    return sorted_words