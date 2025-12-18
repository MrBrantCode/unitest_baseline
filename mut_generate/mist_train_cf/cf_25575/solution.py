"""
QUESTION:
Reverse the order of words in a given sentence. Write a function named `reverse_sentence` that takes a string as input and returns the reversed sentence as a string. The words in the original sentence are separated by a single space and there are no punctuation marks.
"""

def reverse_sentence(sentence):
    """
    Reverses the order of words in a given sentence.

    Args:
        sentence (str): The input sentence.

    Returns:
        str: The reversed sentence.
    """
    return ' '.join(sentence.split()[::-1])