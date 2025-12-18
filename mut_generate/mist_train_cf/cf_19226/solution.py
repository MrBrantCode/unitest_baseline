"""
QUESTION:
Write a function `remove_second_smallest` that takes a list of integers as input. The function should check if the list contains at least 10 elements, then remove the second smallest unique element from the list and add it to a separate list `removed_numbers`. If there are multiple occurrences of the second smallest element, only the first occurrence should be removed. Finally, the original list should be sorted in descending order.
"""

def remove_second_smallest(lst):
    """
    Removes the second smallest unique element from the list if it contains at least 10 elements.
    The removed element is added to a separate list.
    The original list is sorted in descending order.

    Args:
        lst (list): The input list of integers.

    Returns:
        list: The updated list of integers.
        list: A list containing the removed second smallest unique element.
    """
    removed_numbers = []
    if len(lst) >= 10:
        second_smallest = sorted(set(lst))[1]
        index = lst.index(second_smallest)
        removed_numbers.append(lst.pop(index))
        lst.sort(reverse=True)
    return lst, removed_numbers