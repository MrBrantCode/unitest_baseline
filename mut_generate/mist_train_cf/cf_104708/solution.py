"""
QUESTION:
Create a function `remove_duplicates` that takes a list as input and returns a new list containing all unique elements from the original list. The function should use a list comprehension and should not modify the original list.
"""

def remove_duplicates(input_list):
    """
    This function creates a new list containing all unique elements from the input list.
    
    Args:
        input_list (list): The list from which to remove duplicates.
    
    Returns:
        list: A new list containing unique elements from the input list.
    """
    new_list = []
    [new_list.append(x) for x in input_list if x not in new_list]
    return new_list