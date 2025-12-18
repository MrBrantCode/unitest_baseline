"""
QUESTION:
Create a function named `sort_and_filter_words` that takes a list of words as input and returns a sorted list of words in ascending order, excluding any word with more than six letters, and containing only lowercase letters with no duplicates.
"""

def sort_and_filter_words(words):
    return sorted([word.lower() for word in set(words) if len(word) <= 6])