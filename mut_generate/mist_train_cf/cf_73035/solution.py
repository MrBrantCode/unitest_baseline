"""
QUESTION:
Create a function `sort_pairs` that takes a list of pairs as input and returns the sorted list. The pairs should be sorted based on the second element of each pair in ascending order. If the second elements are equal, the pairs should be sorted based on the first element in ascending order.
"""

def sort_pairs(pairs):
    """
    Sorts a list of pairs based on the second element of each pair in ascending order.
    If the second elements are equal, the pairs are sorted based on the first element in ascending order.

    Args:
        pairs (list): A list of pairs.

    Returns:
        list: The sorted list of pairs.
    """
    return sorted(pairs, key=lambda x: (x[1], x[0]))