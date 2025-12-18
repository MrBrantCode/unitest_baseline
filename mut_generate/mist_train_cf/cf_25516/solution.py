"""
QUESTION:
Create a function named `sort_pairs` that sorts an array of pairs in ascending order based on the second element of each pair. The function should take an array of pairs as input and return the sorted array.
"""

def sort_pairs(pairs):
    """
    Sorts an array of pairs in ascending order based on the second element of each pair.

    Args:
        pairs (list): A list of pairs.

    Returns:
        list: The sorted list of pairs.
    """
    return sorted(pairs, key=lambda x: x[1])