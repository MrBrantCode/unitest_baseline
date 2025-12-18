"""
QUESTION:
Write a function named `find_common_elements` that takes two lists as input and returns a list of their common elements without using built-in functions like `set()` or `intersection()`.
"""

def find_common_elements(list1, list2):
    """
    This function takes two lists as input and returns a list of their common elements.
    
    Args:
        list1 (list): The first list.
        list2 (list): The second list.
    
    Returns:
        list: A list of common elements between list1 and list2.
    """
    common_elements = []
    
    for element in list1:
        if element in list2:
            common_elements.append(element)
    
    return common_elements