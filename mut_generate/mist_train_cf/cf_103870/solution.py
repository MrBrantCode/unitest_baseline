"""
QUESTION:
Write a function named `split_and_reverse` that takes a string as input, splits it into a list of words, and returns a list of these words in reverse order, i.e., each word's characters are reversed.
"""

def split_and_reverse(s):
    """
    This function takes a string as input, splits it into a list of words, 
    and returns a list of these words in reverse order, i.e., each word's characters are reversed.

    Args:
        s (str): The input string.

    Returns:
        list: A list of words with characters reversed in reverse order.
    """
    return [word[::-1] for word in s.split()[::-1]]