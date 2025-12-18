"""
QUESTION:
Implement a function `filter_list` that takes a list and a condition as input and returns a new list containing only the elements from the original list that do not meet the condition, maintaining their original order.
"""

def filter_list(lst, condition):
    """
    Filter a list based on a given condition.

    Args:
        lst (list): The list to be filtered.
        condition (function): A function that takes one argument and returns a boolean value.

    Returns:
        list: A new list containing only the elements from the original list that do not meet the condition.
    """
    return [x for x in lst if not condition(x)]