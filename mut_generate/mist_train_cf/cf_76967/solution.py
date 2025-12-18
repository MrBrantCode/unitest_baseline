"""
QUESTION:
Write a function called `replace_indefinite_article` that takes a string as input and returns the string with all instances of the indefinite article "a" replaced with the definite article "the". The function should only replace standalone instances of "a", not instances of "a" that appear within other words.
"""

import re

def replace_indefinite_article(word_string):
    return re.sub(r'\ba\b', 'the', word_string)