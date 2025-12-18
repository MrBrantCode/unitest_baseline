"""
QUESTION:
Create a function `punctuate_numeral_words(s, l)` that takes a string `s` and a list of punctuation symbols `l` as input. The function should return a list of all the words in string `s` that contain numerals and any of the punctuation symbols in `l`. The words should be returned with their original punctuation and in their original order. If the string `s` is empty, does not contain any numerals, or does not contain any of the symbols in `l`, return an empty list.
"""

import re

def punctuate_numeral_words(s, l):
    words = re.findall(r'\b\w+[\w{}]*\b'.format(''.join([re.escape(c) for c in l])), s)
    numeral_words = [word for word in words if any(c.isdigit() for c in word) and any(c in word for c in l)]
    return numeral_words