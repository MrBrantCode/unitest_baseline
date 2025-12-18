"""
QUESTION:
Write a function `find_starting_char` that takes a list of words and a character as input, and returns a list of words that start with the given character. The function should use regular expressions to filter the words.
"""

import re

def find_starting_char(words, char):
    return [word for word in words if re.search("^" + char, word)]