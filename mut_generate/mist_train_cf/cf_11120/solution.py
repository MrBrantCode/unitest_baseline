"""
QUESTION:
Write a function `sort_tuples` that takes a list of tuples as input, where each tuple contains a name and a score. Sort the list in descending order of scores. If multiple tuples have the same score, sort them in ascending order of names.
"""

def sort_tuples(tuples_list):
    """
    Sorts a list of tuples in descending order of scores and ascending order of names.

    Args:
    tuples_list (list): A list of tuples containing names and scores.

    Returns:
    list: The sorted list of tuples.
    """
    return sorted(tuples_list, key=lambda x: (-x[1], x[0]))