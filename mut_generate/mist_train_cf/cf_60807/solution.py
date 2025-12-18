"""
QUESTION:
Write a function named `initial_trio` that takes a string of text as input and returns the first three words from the text. The text is separated by spaces and the function should return the result as a string with the words separated by spaces.
"""

def initial_trio(text):
    """
    Returns the first three words from the input text.

    Args:
        text (str): The input text.

    Returns:
        str: The first three words separated by spaces.
    """
    words = text.split(" ")
    return " ".join(words[:3])