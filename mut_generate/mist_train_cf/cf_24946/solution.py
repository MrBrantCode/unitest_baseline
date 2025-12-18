"""
QUESTION:
Write a function called `compute_probabilities` that takes a list of strings as input and returns a dictionary where the keys are the strings from the input list and the values are their corresponding probabilities. The probability of each string is defined as 1 divided by the total number of strings in the input list.
"""

def compute_probabilities(strings):
    """
    Compute the probability of each string in a given list.

    Args:
    strings (list): A list of strings.

    Returns:
    dict: A dictionary where the keys are the strings from the input list and the values are their corresponding probabilities.
    """
    total_strings = len(strings)
    return {string: 1 / total_strings for string in strings}