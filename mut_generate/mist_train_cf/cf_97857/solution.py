"""
QUESTION:
Create a function `remove_word` that takes two parameters: `text` and `word`, where `text` is the input string and `word` is the word or phrase to be removed. The function should remove all occurrences of `word` from `text`, disregarding case sensitivity and special characters.
"""

import re

def remove_word(text, word):
    """
    Removes all occurrences of a word from a given text, disregarding case sensitivity and special characters.

    Args:
        text (str): The input string.
        word (str): The word or phrase to be removed.

    Returns:
        str: The text with all occurrences of the word removed.
    """
    pattern = re.compile(re.escape(word), re.IGNORECASE)
    return pattern.sub("", text)