"""
QUESTION:
Write a function `sort_words` that takes a string as input, splits it into words, removes any empty strings and words with less than three characters, trims leading and trailing whitespace from each word, and returns the resulting words sorted in descending order of their lengths. If two words have the same length, they should be sorted alphabetically.
"""

def sort_words(s):
    """
    Sorts the words in a given string by length in descending order and then alphabetically.

    Args:
    s (str): The input string.

    Returns:
    list: A list of words sorted by length in descending order and then alphabetically.
    """
    words = [word.strip() for word in s.split() if len(word.strip()) >= 3]
    return sorted(words, key=lambda x: (-len(x), x))