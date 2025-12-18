"""
QUESTION:
Write a function named `format_list` that takes a list of words as input. The function should return a single string with the words sorted in reverse alphabetical order, separated by a comma and a space, and each word surrounded by parentheses.
"""

def format_list(lst):
    """
    This function formats a list of words into a string, sorted in reverse alphabetical order,
    with each word surrounded by parentheses and separated by a comma and a space.

    Args:
        lst (list): A list of words.

    Returns:
        str: A formatted string with the words sorted in reverse alphabetical order.
    """
    return ', '.join('({})'.format(word) for word in sorted(lst, reverse=True))