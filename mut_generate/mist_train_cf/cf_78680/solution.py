"""
QUESTION:
Write a function named `generate_synopsis` that takes two parameters: `text` and `max_words`. The function should truncate the input `text` to `max_words` words and return the truncated text. The function must not use any built-in or third-party libraries/formatters to format the text. The function should be able to handle cases where the input `text` is longer than `max_words`.
"""

def generate_synopsis(text, max_words):
    """
    Truncates the input text to max_words words.

    Args:
        text (str): The input text to be truncated.
        max_words (int): The maximum number of words allowed in the output text.

    Returns:
        str: The truncated text.
    """
    words = text.split()
    if len(words) > max_words:
        words = words[:max_words]
    synopsis = ' '.join(words)
    return synopsis