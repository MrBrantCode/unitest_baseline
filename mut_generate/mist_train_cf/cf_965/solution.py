"""
QUESTION:
Create a function `insert_element_at_index` that inserts an element into a sorted list at a specified index while maintaining the list's sorted order, without using built-in list manipulation functions like insert(), append(), or extend(). The function should achieve this with a time complexity of O(n) and a space complexity of O(1), where n is the length of the list.
"""

def insert_element_at_index(sorted_list, inserted_element, index):
    """
    Inserts an element into a sorted list at a specified index while maintaining the list's sorted order.

    Args:
        sorted_list (list): The input sorted list.
        inserted_element: The element to be inserted into the list.
        index (int): The index at which the element is to be inserted.

    Returns:
        list: The modified sorted list with the element inserted.
    """
    sorted_list.append(inserted_element)
    i = len(sorted_list) - 1
    while i > index:
        sorted_list[i], sorted_list[i-1] = sorted_list[i-1], sorted_list[i]
        i -= 1
    return sorted_list