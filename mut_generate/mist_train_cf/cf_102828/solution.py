"""
QUESTION:
Create a function named `filter_array` that takes two parameters: a list `lst` and a function `criteria`. The function should filter out elements in `lst` that do not meet the given `criteria` and return the remaining elements in descending order. The `criteria` parameter is a function that takes one argument and returns a boolean value. The function should not modify the original list.
"""

def filter_array(lst, criteria):
    """
    Filters out elements in lst that do not meet the given criteria and returns the remaining elements in descending order.

    Args:
        lst (list): The input list to be filtered.
        criteria (function): A function that takes one argument and returns a boolean value.

    Returns:
        list: The filtered list in descending order.
    """
    return sorted([num for num in lst if criteria(num)], reverse=True)