"""
QUESTION:
Create a function named `filter_words` that takes a list of strings as input. The function should return a list of words that do not contain the letter 'a' and have an even number of characters.
"""

def filter_words(words):
    """
    This function filters a list of words and returns a new list containing only the words 
    that do not contain the letter 'a' and have an even number of characters.

    Parameters:
    words (list): A list of strings.

    Returns:
    list: A list of filtered words.
    """
    return [word for word in words if 'a' not in word and len(word) % 2 == 0]