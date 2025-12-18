"""
QUESTION:
Create a function `create_variable` that stores a given list of elements in a variable. The list can contain any data type, must have a maximum of 5 elements, and all elements must be unique. Implement the function to ensure these conditions are met.
"""

def create_variable(input_list):
    """
    Creates a variable to store a given list of elements, ensuring the list has a maximum of 5 unique elements.
    
    Args:
        input_list (list): A list containing any data type.
    
    Returns:
        list: A list of unique elements if the input list has 5 or fewer elements; otherwise, None.
    """

    # Check if the list has more than 5 elements
    if len(input_list) > 5:
        return None
    
    # Convert the list to a set to eliminate duplicates
    unique_set = set(input_list)
    
    # Check if the set has the same length as the original list
    if len(unique_set) != len(input_list):
        return None
    
    # Convert the set back to a list
    unique_list = list(unique_set)
    
    return unique_list