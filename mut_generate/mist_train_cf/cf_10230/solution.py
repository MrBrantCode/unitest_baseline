"""
QUESTION:
Write a function called `reverse_and_capitalize` that takes a string of words as input, reverses the order of the words, and capitalizes each word. The function should return the resulting string. The input string contains only words separated by spaces and does not contain any punctuation or special characters.
"""

def reverse_and_capitalize(s):
    """
    Reverses the order of words in a string and capitalizes each word.

    Args:
        s (str): A string of words separated by spaces.

    Returns:
        str: The resulting string with reversed word order and capitalized words.
    """
    return ' '.join(word.upper() for word in s.split()[::-1])