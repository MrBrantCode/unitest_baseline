"""
QUESTION:
Write a function `find_common_elements` that takes two lists `list1` and `list2` of varying lengths as input and returns a list of unique common elements between the two lists. The function should not use any built-in functions or libraries for set operations and should be optimized for time complexity.
"""

def find_common_elements(list1, list2):
    """
    This function takes two lists of varying lengths as input and returns a list of unique common elements between the two lists.

    Args:
        list1 (list): The first list.
        list2 (list): The second list.

    Returns:
        list: A list of unique common elements between the two lists.
    """
    
    # Create empty list to hold common elements
    common_elements = []
    
    # Create dictionary to hold elements in list1
    elements = {}
    
    # Iterate over list1 and add elements in the dictionary
    for i in list1:
        if i not in elements:
            elements[i] = True
    
    # Iterate over list2 and add common elements in the list
    for i in list2:
        if i in elements and i not in common_elements:
            common_elements.append(i)
            
    return common_elements