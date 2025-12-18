"""
QUESTION:
Write a function `filter_and_sort_words` that takes a list of words as input, filters out any word with more than six letters, converts the remaining words to lowercase, removes duplicates, and returns them in ascending order.
"""

def filter_and_sort_words(words):
    return sorted([word.lower() for word in set(words) if len(word) <= 6])