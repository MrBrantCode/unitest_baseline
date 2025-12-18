"""
QUESTION:
Implement a function `find_first_and_last` that takes a list `lst` and an element `x` as input, and returns a tuple containing the first and last indices of `x` in `lst`. If `x` is not found in `lst`, return `(-1, -1)`. The function should have a time complexity of O(n) and only make a single pass through the list.
"""

def find_first_and_last(lst, x):
    """
    Find the first and last indices of an element in a list.

    Args:
        lst (list): The list to search in.
        x: The element to search for.

    Returns:
        tuple: A tuple containing the first and last indices of x in lst. 
               Returns (-1, -1) if x is not found in lst.
    """
    first = -1
    last = -1
    for i in range(len(lst)):
        if lst[i] == x:
            if first == -1:
                first = i
            last = i
    return first, last