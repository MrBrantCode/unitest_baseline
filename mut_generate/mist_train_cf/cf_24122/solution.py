"""
QUESTION:
Create a function named `create_reverse_lookup` that takes a list of words as input and returns a dictionary where each unique word is a key and its corresponding value is a list of indices where the word appears in the input list. The function should handle duplicate words and their corresponding indices correctly.
"""

def create_reverse_lookup(words):
    """
    Creates a dictionary where each unique word is a key and its corresponding value 
    is a list of indices where the word appears in the input list.

    Args:
        words (list): A list of words.

    Returns:
        dict: A dictionary with words as keys and their indices as values.
    """
    return {word: [i for i, v in enumerate(words) if v == word] for word in set(words)}