"""
QUESTION:
Write a function called `count_occurrences` that takes a list `lst`, an element, and a data type as input, and returns the count of occurrences of the element in the list while ignoring any occurrences within nested sublists and considering only elements of the specified data type. The function should not modify the original list and should handle lists containing elements of various data types.
"""

def count_occurrences(lst, element, data_type):
    """
    Counts the occurrences of an element in a list while ignoring any occurrences 
    within nested sublists and considering only elements of the specified data type.

    Args:
        lst (list): The list to search in.
        element: The element to search for.
        data_type (type): The data type of the element.

    Returns:
        int: The count of occurrences of the element.
    """

    count = 0

    def check_occurrences(sublst):
        nonlocal count
        for item in sublst:
            if isinstance(item, list):
                check_occurrences(item)
            elif isinstance(item, data_type) and item == element:
                count += 1

    check_occurrences(lst)
    return count