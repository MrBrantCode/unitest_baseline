"""
QUESTION:
Create a function called `invert_sentence` that takes a sentence as input and returns the sentence with the order of words reversed. The function should split the sentence into words, reverse the order of the words, and then join them back together into a sentence.
"""

def invert_sentence(sentence):
    """
    Inverts the order of words in a sentence.

    Args:
        sentence (str): The input sentence.

    Returns:
        str: The sentence with the order of words reversed.
    """
    words = sentence.split()
    words.reverse()
    return " ".join(words)