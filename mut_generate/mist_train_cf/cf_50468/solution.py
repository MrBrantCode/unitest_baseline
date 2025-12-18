"""
QUESTION:
Replace the indefinite article "a" with the definite article "the" in a given sentence, without substituting "a" when it is part of another word. Write a function named `replace_article(sentence)` that takes a string as input and returns the modified sentence. The function should ensure that only standalone "a" is replaced, ignoring instances of "a" within other words.
"""

import re

def replace_article(sentence):
    # we use optional space ("\s?") to handle a followed by punctuation without space.
    sentence = re.sub(r'\ba\b', 'the', sentence)
    return sentence