"""
QUESTION:
Write a function `sort_words` that takes a list of words as an argument and returns a new list where the words are sorted first by their length in ascending order, and then alphabetically in ascending order. The function should be able to handle lists with up to 10,000 words and sort them efficiently within a reasonable time frame.
"""

def sort_words(words):
    """
    Sorts a list of words in ascending order based on their length, and then in alphabetical order.

    Args:
        words (list): A list of words to be sorted.

    Returns:
        list: A new list of sorted words.
    """
    return sorted(words, key=lambda x: (len(x), x))