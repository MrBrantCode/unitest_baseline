"""
QUESTION:
Write a function called append_or_remove_and_sort that takes a list of items and a target item as input. If the target item is not in the list, append it to the end of the list. If the target item is in the list, remove all instances of it and print the number of occurrences removed. Finally, sort the list in descending order and return it.
"""

def append_or_remove_and_sort(lst, target):
    """
    This function appends or removes a target item from a list and sorts the list in descending order.

    If the target item is not in the list, it is appended to the end.
    If the target item is in the list, all instances are removed and the number of occurrences is printed.

    Args:
        lst (list): The input list of items.
        target (any): The target item to be appended or removed.

    Returns:
        list: The updated list sorted in descending order.
    """

    if target not in lst:
        lst.append(target)
    else:
        count = lst.count(target)
        lst = [item for item in lst if item != target]
        print(f"Removed {count} occurrences of '{target}'")

    lst.sort(reverse=True)
    return lst