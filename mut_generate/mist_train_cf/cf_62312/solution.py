"""
QUESTION:
Write a function `remove_spaces(sentence)` that takes a string `sentence` as input, removes all occurrences of consecutive spaces (two or more) and replaces them with a single space, and also removes any leading or trailing spaces.
"""

def remove_spaces(sentence):
    no_consecutive_spaces = ' '.join(sentence.split())
    return no_consecutive_spaces