"""
QUESTION:
Create two functions, `is_element_present(lst, element)` and `find_element_index(lst, element)`, that take a list `lst` of integers and/or floats and an element as input. The functions should first determine the median of the list by sorting it. The `is_element_present` function should return `True` if the element is present in the list and is greater than or equal to the median, and `False` otherwise. The `find_element_index` function should return the index of the first occurrence of the element in the list if it is greater than or equal to the median, and -1 otherwise. The functions should be able to handle large lists of up to 10^6 elements efficiently.
"""

def is_element_present(lst, element):
    """
    Checks if an element is present in a list and is greater than or equal to the median.
    
    Parameters:
    lst (list): A list of integers and/or floats.
    element: The element to be checked.
    
    Returns:
    bool: True if the element is present in the list and is greater than or equal to the median, False otherwise.
    """
    sorted_lst = sorted(lst)
    median = sorted_lst[len(sorted_lst) // 2]
    return element >= median and element in lst

def find_element_index(lst, element):
    """
    Finds the index of an element in a list if it is greater than or equal to the median.
    
    Parameters:
    lst (list): A list of integers and/or floats.
    element: The element to be found.
    
    Returns:
    int: The index of the first occurrence of the element if it is greater than or equal to the median, -1 otherwise.
    """
    sorted_lst = sorted(lst)
    median = sorted_lst[len(sorted_lst) // 2]
    if element >= median and element in lst:
        return lst.index(element)
    else:
        return -1