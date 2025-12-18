"""
QUESTION:
Create a function named `find_words` that takes a string `text` as input. The function should return a set of unique words from the input string that contain the letters "a", "b", and "c" in any order, regardless of case. The function should ignore non-word characters and return each word only once.
"""

import re

def find_words(text):
    pattern = re.compile(r'\b(?=\w*a)(?=\w*b)(?=\w*c)\w+\b', re.I)
    matches = pattern.findall(text)
    return set(matches)