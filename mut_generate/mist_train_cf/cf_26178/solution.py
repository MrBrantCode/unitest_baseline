"""
QUESTION:
Sort a given list of pairs by the second element of each pair. The list can contain duplicate pairs and pairs can be in any order. Create a function `sort_pairs_by_second_element` that takes the list as input and returns the sorted list. The function should use a stable sort, preserving the original order of pairs with the same second element.
"""

def sort_pairs_by_second_element(pairs):
    """
    Sorts a given list of pairs by the second element of each pair.
    
    This function takes a list of pairs as input, sorts it based on the second element of each pair, 
    and returns the sorted list. It uses a stable sort to preserve the original order of pairs 
    with the same second element.

    Args:
        pairs (list): A list of pairs.

    Returns:
        list: The sorted list of pairs.
    """
    return sorted(pairs, key=lambda x: x[1])