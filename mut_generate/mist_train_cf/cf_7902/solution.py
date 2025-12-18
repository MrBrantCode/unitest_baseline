"""
QUESTION:
Write a function named `find_element` that takes a nested array and an element as input. The function should return the index position of the element in the nested array. If the element is in a subarray, return the index of the subarray and the index of the element within the subarray. If the element is not in a subarray, return only its index. If the element is not found, return a message stating that the element is not present. The function should work for any type of element and any level of nesting.
"""

def find_element(array, element):
    """
    This function finds the index position of an element in a nested array.
    
    Args:
    array (list): The nested array to search in.
    element: The element to search for.
    
    Returns:
    list or str: The index position of the element if found, otherwise a message stating that the element is not present.
    """
    for i, subarray in enumerate(array):
        if isinstance(subarray, list): # check if the current element is a list
            if element in subarray:
                return [i, subarray.index(element)]
        elif element == subarray:
            return [i]
    
    return "Element is not present"