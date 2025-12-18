"""
QUESTION:
Write a function called `intersection` that takes two lists of integers as input and returns a list of integers representing their intersection. The function should only include elements that are present in both input lists.
"""

def intersection(List1, List2):
    """
    This function takes two lists of integers as input and returns a list of integers representing their intersection.

    Args:
        List1 (list): The first list of integers.
        List2 (list): The second list of integers.

    Returns:
        list: A list of integers representing the intersection of List1 and List2.
    """
    return list(filter(lambda x: x in List1, List2))