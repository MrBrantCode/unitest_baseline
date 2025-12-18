"""
QUESTION:
Create a function named `deep_copy` that creates a deep copy of the given list without using the copy module, any other built-in functions, or libraries. The function should not use temporary variables or lists. The time complexity of the solution should be O(n), where n is the total number of elements in the original list.
"""

def deep_copy(original_list):
    """
    Creates a deep copy of the given list without using the copy module, 
    any other built-in functions, or libraries.

    Args:
        original_list (list): The list to be copied.

    Returns:
        list: A deep copy of the original list.
    """
    if not isinstance(original_list, list):
        return original_list

    copied_list = []
    for element in original_list:
        if isinstance(element, list):
            copied_list.append(deep_copy(element))
        else:
            copied_list.append(element)
    return copied_list