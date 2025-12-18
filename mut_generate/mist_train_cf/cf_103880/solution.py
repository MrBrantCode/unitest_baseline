"""
QUESTION:
Write a function `get_sorted_combinations` that takes two lists as input and returns all possible pairs of elements, where each pair contains one element from each list. The output should be sorted in descending order. The function should be able to handle any two input lists.
"""

def get_sorted_combinations(list1, list2):
    """
    Returns all possible pairs of elements from two input lists, 
    where each pair contains one element from each list, 
    sorted in descending order.

    Args:
        list1 (list): The first input list.
        list2 (list): The second input list.

    Returns:
        list: A list of tuples, each containing a pair of elements from the input lists.
    """
    return sorted([(x, y) for x in list1 for y in list2], reverse=True)