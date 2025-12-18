"""
QUESTION:
Write a function `sort_reversed_words` that takes a list of strings as input. The function should reverse each word in the list, then sort the list in alphabetical order. The function should return the sorted list of reversed words.
"""

def sort_reversed_words(lexical_items):
    return sorted([word[::-1] for word in lexical_items])