"""
QUESTION:
Write a function `top_strings` that takes a list of strings as input and returns a dictionary containing the top 10 most common strings in the list, with their corresponding frequencies.
"""

from collections import Counter

def top_strings(strings):
    """
    Returns a dictionary containing the top 10 most common strings in the input list, 
    with their corresponding frequencies.

    Args:
        strings (list): A list of strings.

    Returns:
        dict: A dictionary with the top 10 most common strings and their frequencies.
    """
    freq = Counter(strings)
    return dict(freq.most_common(10))