"""
QUESTION:
Write a function called `sort_sentence` that takes a list of words as input and returns a string where the words are arranged in alphabetical order, separated by a space. The input is a list of words, and the function should return a single string.
"""

def sort_sentence(words):
    sorted_words = sorted(words)
    sorted_sentence = ' '.join(sorted_words)
    return sorted_sentence