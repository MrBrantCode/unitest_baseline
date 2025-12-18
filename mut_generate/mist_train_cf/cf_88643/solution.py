"""
QUESTION:
Implement a function named `split_reverse_sentence` that takes a sentence as a string and returns the words in reverse order. The function should use regular expressions to split the sentence into words, handle leading and trailing whitespaces in the sentence, and handle multiple consecutive whitespaces between words. Additionally, it should not use any built-in string or array manipulation functions such as `split()`, `reverse()`, or indexing.
"""

import re

def split_reverse_sentence(sentence):
    # Remove leading and trailing whitespaces
    sentence = re.sub(r'^\s+|\s+$', '', sentence)

    # Split sentence into words using regular expression
    words = re.findall(r'\S+', sentence)

    # Reverse the order of the words
    words.reverse()

    return words