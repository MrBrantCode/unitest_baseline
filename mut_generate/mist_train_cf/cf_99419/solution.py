"""
QUESTION:
Write a function called `invert_sentence` that takes a sentence as input, reverses the order of its words, and returns the inverted sentence. The function should work with any sentence, regardless of the number of words or their lengths.
"""

def invert_sentence(sentence):
    """
    Inverts the order of words in a sentence.

    Args:
        sentence (str): The input sentence.

    Returns:
        str: The inverted sentence.
    """
    words = sentence.split()
    words.reverse()
    return " ".join(words)