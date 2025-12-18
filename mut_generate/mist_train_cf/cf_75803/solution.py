"""
QUESTION:
Write a function `words_string(s, target)` that takes a string `s` and a target word `target` as input. The string `s` contains words separated by commas, spaces, or a combination of both. The function should split the string into words, remove all occurrences of the target word, reverse the remaining words, and return them in their original order.
"""

def words_string(s, target):
    """Splits a string into words, removes all occurrences of a target word, 
    reverses the remaining words, and returns them in their original order.

    Args:
    s (str): A string containing words separated by commas, spaces, or both.
    target (str): The target word to be removed.

    Returns:
    list: A list of words with the target word removed and the remaining words reversed.
    """
    words = s.replace(",", "").split()
    result = [word[::-1] for word in words if word != target]
    return result