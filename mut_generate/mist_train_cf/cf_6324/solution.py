"""
QUESTION:
Write a function `remove_occurrences(lst, element)` that removes all occurrences of a specified element from a given list in-place and returns the modified list. The function should have a time complexity of O(n), where n is the length of the list, and should not use built-in list methods such as remove().
"""

def remove_occurrences(lst, element):
    """
    Removes all occurrences of a specified element from a given list in-place and returns the modified list.

    Args:
        lst (list): The input list.
        element: The element to be removed.

    Returns:
        list: The modified list with all occurrences of the specified element removed.

    Time Complexity:
        O(n), where n is the length of the list.
    """
    if len(lst) == 0:
        return lst
    
    i = 0
    while i < len(lst):
        if lst[i] == element:
            lst.pop(i)
        else:
            i += 1
    
    return lst