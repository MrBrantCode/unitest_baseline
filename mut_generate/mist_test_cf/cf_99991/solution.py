"""
QUESTION:
Create a function called `remove_word` that takes two parameters, `text` and `word`, and returns the text after removing all occurrences of the specified word or phrase. The function should be case-insensitive and ignore special characters.
"""

import re
def remove_word(text, word):
    """
    Removes all occurrences of the specified word or phrase from the given text.
    
    The function is case-insensitive and ignores special characters.
    
    Parameters:
    text (str): The original text.
    word (str): The word or phrase to be removed.
    
    Returns:
    str: The text after removing all occurrences of the specified word or phrase.
    """
    pattern = re.compile(re.escape(word), re.IGNORECASE)
    return pattern.sub("", text)