"""
QUESTION:
Create a function `remove_all_occurrences` that takes a string `text` and a word `target_word` as input. The function should return the string `text` with all occurrences of `target_word` removed.
"""

def remove_all_occurrences(text, target_word):
    """
    This function removes all occurrences of a target word from a given text.

    Args:
        text (str): The input text.
        target_word (str): The word to be removed.

    Returns:
        str: The text with all occurrences of the target word removed.
    """
    return ' '.join(word for word in text.split() if word != target_word)