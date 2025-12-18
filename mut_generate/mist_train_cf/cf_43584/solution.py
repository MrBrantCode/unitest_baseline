"""
QUESTION:
Create a function `ascii_dict` that takes a list of characters as input and returns a dictionary where the keys are the characters from the list and the values are their corresponding ASCII values. The function should use dictionary comprehension and the `ord()` function to obtain ASCII values.
"""

def ascii_dict(chars):
    """
    Create a dictionary where keys are characters from the input list and values are their corresponding ASCII values.

    Args:
        chars (list): A list of characters.

    Returns:
        dict: A dictionary with characters as keys and their ASCII values as values.
    """
    return {key: ord(key) for key in chars}