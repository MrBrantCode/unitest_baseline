"""
QUESTION:
Write a function named `count_words` that takes a string as input and returns the number of words in the string. A word is defined as a sequence of alphabetic characters separated by at least one space, punctuation mark, or digit. The function should be case sensitive and use regular expressions.
"""

import re

def count_words(string):
    pattern = r'\b[a-zA-Z]+\b'
    word_list = re.findall(pattern, string)
    return len(word_list)