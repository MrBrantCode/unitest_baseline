"""
QUESTION:
Write a function named `remove_word` that takes in a string `text` and a string `word`, and returns the text with all occurrences of the `word` removed, regardless of case sensitivity or presence of special characters.
"""

import re

def remove_word(text, word):
    """
    Removes all occurrences of a word from a given text, 
    regardless of case sensitivity or presence of special characters.

    Args:
        text (str): The original text.
        word (str): The word to remove.

    Returns:
        str: The text with all occurrences of the word removed.
    """
    pattern = re.compile(re.escape(word), re.IGNORECASE)
    return pattern.sub("", text)