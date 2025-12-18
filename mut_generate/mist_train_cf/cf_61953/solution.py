"""
QUESTION:
Develop a function named `min_sentence_length` that takes a list of sentences as input and returns the sentence with the minimum string length. The function should return the first sentence it encounters if multiple sentences have the same minimum length.
"""

def min_sentence_length(sentences):
    """
    Returns the sentence with the minimum string length from a list of sentences.

    If multiple sentences have the same minimum length, returns the first one encountered.

    Args:
        sentences (list): A list of sentences.

    Returns:
        str: The sentence with the minimum length.
    """
    return min(sentences, key=len)