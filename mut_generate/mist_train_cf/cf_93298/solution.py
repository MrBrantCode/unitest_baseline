"""
QUESTION:
Write a function `find_common_elements` that takes two lists as input and returns a list containing only the elements common to both input lists, without duplicates.
"""

def find_common_elements(list1, list2):
    """
    Returns a list containing only the elements common to both input lists, without duplicates.

    Args:
        list1 (list): The first input list.
        list2 (list): The second input list.

    Returns:
        list: A list of common elements without duplicates.
    """
    common_elements = []
    for element in list1:
        if element in list2 and element not in common_elements:
            common_elements.append(element)
    return common_elements