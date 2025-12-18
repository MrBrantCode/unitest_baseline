"""
QUESTION:
Write a function called `filter_words` that takes a list of words as input, filters out the words that do not contain the letter 'a' (ignoring case sensitivity), removes duplicates, and returns the resulting list in alphabetical order. The function should be able to handle lists with up to 100 words.
"""

def filter_words(words):
    """Filters out the words that do not contain the letter 'a' (ignoring case sensitivity), removes duplicates, and returns the resulting list in alphabetical order."""
    return sorted(set(word.lower() for word in words if 'a' in word.lower()))