"""
QUESTION:
Write a function `sort_by_length(words)` that takes a list of words as input and returns a new sorted list containing only the words with a length greater than 5 characters. The sorting should be based on the length of the words first and then alphabetical order, with a time complexity of O(n log n).
"""

def sort_by_length(words):
    return sorted(filter(lambda x: len(x) > 5, words), key=lambda x: (len(x), x))