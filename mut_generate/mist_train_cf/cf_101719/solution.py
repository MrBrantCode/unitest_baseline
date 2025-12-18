"""
QUESTION:
Write a function called `sorted_words` that takes a list of words as input, removes duplicates, converts all words to lowercase, excludes any word with more than six letters, and returns the resulting list in ascending order.
"""

def sorted_words(words):
    """Takes a list of words, removes duplicates, converts to lowercase, 
    excludes words with more than six letters, and returns the list in ascending order."""
    return sorted([word.lower() for word in set(words) if len(word) <= 6])