"""
QUESTION:
Write a function `sort_dictionary_by_meanings` that takes a dictionary as input, where each key is a word and its corresponding value is a list of meanings. The function should return the words sorted by the number of meanings they have. If two words have the same number of meanings, the order of these words is not specified. The dictionary should be in the format {'word': ['meaning1', 'meaning2', ...]}.
"""

def sort_dictionary_by_meanings(dictionary):
    """
    Sorts a dictionary by the number of meanings each word has.

    Args:
        dictionary (dict): A dictionary where each key is a word and its corresponding value is a list of meanings.

    Returns:
        list: A list of words sorted by the number of meanings they have.
    """
    return sorted(dictionary, key=lambda word: len(dictionary[word]))