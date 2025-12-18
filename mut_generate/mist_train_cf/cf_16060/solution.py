"""
QUESTION:
Create a function named `find_common_elements` that takes two lists, `list1` and `list2`, as parameters and returns a new list containing the elements that are common to both lists. The function must have a time complexity of O(n^2), where n is the length of the longer list.
"""

def find_common_elements(list1, list2):
    """
    This function finds the common elements between two lists.
    
    Args:
        list1 (list): The first list.
        list2 (list): The second list.
    
    Returns:
        list: A new list containing the elements common to both input lists.
    """
    common_elements = []
    for element1 in list1:
        for element2 in list2:
            if element1 == element2:
                common_elements.append(element1)
                break
    return common_elements