"""
QUESTION:
Create a function `remove_element(lst, element)` that takes a list `lst` and an element as input. Remove all instances of the given element from the list while preserving the order of the remaining elements. Return the modified list and the number of elements removed. If the input list is empty, return an error message. If the element to be removed is not present in the list, return -1 as the number of elements removed.
"""

def remove_element(lst, element):
    """
    Removes all instances of the given element from the list while preserving the order of the remaining elements.
    
    Args:
        lst (list): Input list.
        element: Element to be removed.
    
    Returns:
        tuple: Modified list and the number of elements removed. If the input list is empty, returns an error message.
    """

    if len(lst) == 0:
        return "Error: The input list is empty."

    if element not in lst:
        return lst, -1

    count_removed = 0
    new_lst = []

    for i in lst:
        if i != element:
            new_lst.append(i)
        else:
            count_removed += 1

    return new_lst, count_removed