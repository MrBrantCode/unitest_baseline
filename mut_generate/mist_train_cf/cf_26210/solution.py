"""
QUESTION:
Create a function `unique_elements` that takes a list as input and returns a list with only the unique elements. The order of the elements in the original list can be lost.
"""

def unique_elements(input_list):
    """
    This function takes a list as input and returns a list with only the unique elements.
    
    Args:
        input_list (list): The list from which to extract unique elements.
    
    Returns:
        list: A list containing unique elements from the input list.
    """
    return list(set(input_list))