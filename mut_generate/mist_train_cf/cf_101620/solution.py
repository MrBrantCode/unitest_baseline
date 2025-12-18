"""
QUESTION:
Write a function `sort_sentence` that takes a list of words as input, sorts them in alphabetical order, and returns the sorted words as a single string separated by spaces.
"""

def sort_sentence(words):
    sorted_words = sorted(words)
    sorted_sentence = ' '.join(sorted_words)
    return sorted_sentence