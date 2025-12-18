"""
QUESTION:
Write a function called `concatenate_lists` that takes two input lists `list1` and `list2` and returns a new list containing all elements from both lists. The function must not use the "+" operator or the "extend" method for concatenation.
"""

def concatenate_lists(list1, list2):
    """
    Concatenates two input lists without using the "+" operator or the "extend" method.

    Args:
        list1 (list): The first list to concatenate.
        list2 (list): The second list to concatenate.

    Returns:
        list: A new list containing all elements from both input lists.
    """
    return list(list1) + list(list2)