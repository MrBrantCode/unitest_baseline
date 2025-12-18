"""
QUESTION:
Write a function named `find_common_elements` that takes two lists as parameters and returns a list containing the common elements that occur in both lists. The function should have a time complexity of O(n), where n is the length of the longer list. The function should not use any built-in Python functions that directly solve the problem, such as intersection or set operations.
"""

def find_common_elements(list1, list2):
    """
    This function takes two lists as parameters and returns a list containing the common elements that occur in both lists.
    
    The function achieves a time complexity of O(n), where n is the length of the longer list, by utilizing a dictionary to store the count of each element in the first list.
    
    :param list1: The first list to compare
    :param list2: The second list to compare
    :return: A list containing the common elements that occur in both lists
    """
    
    # Check if either list is empty
    if len(list1) == 0 or len(list2) == 0:
        return []
    
    # Create a dictionary to store the count of each element in list1
    element_count = {}
    for element in list1:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    
    # Iterate through list2 and check if each element is present in element_count
    common_elements = []
    for element in list2:
        if element in element_count and element_count[element] > 0:
            common_elements.append(element)
            element_count[element] -= 1
    
    return common_elements