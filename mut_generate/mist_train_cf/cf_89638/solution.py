"""
QUESTION:
Implement a function `linear_search(lst, target)` that performs a linear search for the `target` element in a list of integers `lst` and returns the index of the first occurrence of the found element. If the element is not found, return -1. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the list. The list may contain duplicates.
"""

def linear_search(lst, target):
    """
    Performs a linear search for the target element in a list of integers.

    Args:
        lst (list): A list of integers.
        target (int): The target element to search for.

    Returns:
        int: The index of the first occurrence of the target element if found, -1 otherwise.

    Time complexity: O(n)
    Space complexity: O(1)
    """
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1