"""
QUESTION:
Create a function `find_common_elements` that takes two lists of integers as input and returns a new list containing their common elements in descending order, without duplicates. The function should achieve this in a time complexity of O(n log n), where n is the total number of elements in both lists.
"""

def find_common_elements(list1, list2):
    """
    This function finds the common elements of two lists in descending order without duplicates.
    
    Parameters:
    list1 (list): The first list of integers.
    list2 (list): The second list of integers.
    
    Returns:
    list: A list of common elements in descending order without duplicates.
    """
    # Convert the lists to sets to remove duplicates and find common elements
    common_elements = set(list1).intersection(set(list2))
    
    # Convert the set back to a list and sort it in descending order
    common_elements_list = sorted(list(common_elements), reverse=True)
    
    return common_elements_list