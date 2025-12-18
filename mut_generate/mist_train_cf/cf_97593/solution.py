"""
QUESTION:
Write a function called `sort_words` that takes a list of words as input and returns the list sorted in alphabetical order based on the second letter, then by the third letter, then by the first letter. The function should also remove any duplicate words from the list before sorting. Assume that all input words have at least three characters.
"""

def sort_words(words):
    # Remove duplicates
    words = list(set(words))
    # Sort by second letter, then by third letter, then by first letter
    words.sort(key=lambda x: (x[1], x[2], x[0]))
    return words