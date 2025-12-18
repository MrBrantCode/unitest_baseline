"""
QUESTION:
Write a function `remove_word` that takes two parameters: `text` and `word`. The function should remove all occurrences of `word` from `text`, regardless of case sensitivity or presence of special characters. The function should return the resulting text after removing all occurrences of `word`.
"""

import re

def remove_word(text, word):
    """
    Removes all occurrences of a word from a given text, 
    regardless of case sensitivity or presence of special characters.

    Parameters:
    text (str): The original text.
    word (str): The word to be removed.

    Returns:
    str: The resulting text after removing all occurrences of the word.
    """
    pattern = re.compile(re.escape(word), re.IGNORECASE)
    return pattern.sub("", text)