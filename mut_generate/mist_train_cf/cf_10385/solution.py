"""
QUESTION:
Write a function `combine_lists` that takes two lists of integers as input and returns a list of tuples, where each tuple contains one element from the first list and the corresponding element from the second list at the same index. The function should exclude any elements from the first list that are divisible by 3.
"""

def combine_lists(list1, list2):
    """
    This function combines two lists of integers into a list of tuples, 
    excluding elements from the first list that are divisible by 3.

    Args:
        list1 (list): The first list of integers.
        list2 (list): The second list of integers.

    Returns:
        list: A list of tuples, where each tuple contains one element from the first list 
              and the corresponding element from the second list at the same index.
    """
    return [(x, y) for x, y in zip(list1, list2) if x % 3 != 0]