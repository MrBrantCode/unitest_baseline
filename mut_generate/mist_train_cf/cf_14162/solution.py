"""
QUESTION:
Write a function called `to_camel_case` that takes a sentence as input and returns the sentence converted to camelCase. The function should remove all spaces, handle punctuation marks, ensure each word begins with a capital letter, and handle sentences with multiple consecutive spaces.
"""

def to_camel_case(sentence):
    """
    Converts a sentence to camelCase.

    Args:
    sentence (str): The input sentence.

    Returns:
    str: The sentence converted to camelCase.
    """
    sentence = ''.join(e for e in sentence if e.isalnum() or e.isspace())
    words = sentence.split()
    return ''.join(word.capitalize() for word in words)