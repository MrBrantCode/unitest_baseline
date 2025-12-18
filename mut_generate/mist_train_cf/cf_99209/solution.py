"""
QUESTION:
Write a Python function called `sort_sentence` that takes a list of words as input, sorts them in alphabetical order, and returns the resulting sentence as a string. The sentence should be formatted with words separated by a single space.
"""

def sort_sentence(words):
    sorted_words = sorted(words)
    sorted_sentence = ' '.join(sorted_words)
    return sorted_sentence