"""
QUESTION:
Write a function `count_vowels_in_valid_word` that takes a string as input and returns the number of vowels in the word if it is a valid English word; otherwise, return -1. Assume a list of valid English words is predefined.
"""

def count_vowels_in_valid_word(word, valid_words):
    """
    This function counts the number of vowels in a given word if it's a valid English word.

    Args:
        word (str): The input word to be checked and counted for vowels.
        valid_words (list): A predefined list of valid English words.

    Returns:
        int: The number of vowels in the word if it's valid, -1 otherwise.
    """
    if word in valid_words:
        return sum(1 for char in word if char.lower() in 'aeiouy')
    else:
        return -1