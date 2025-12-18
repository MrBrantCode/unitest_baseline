"""
QUESTION:
Create a function named `flatten_and_sort` that takes a list of lists as input. This function should return a list containing all unique elements from the input list, sorted in ascending order.
"""

def flatten_and_sort(list_of_lists):
    """Takes a list of lists, removes duplicates, and sorts the elements in ascending order."""
    
    flattened_list = []
    
    for element in list_of_lists:
        if isinstance(element, list):
            for nested_element in element:
                flattened_list.append(nested_element)
        else:
            flattened_list.append(element)
    
    flattened_list = list(set(flattened_list))
    flattened_list.sort()
    
    return flattened_list