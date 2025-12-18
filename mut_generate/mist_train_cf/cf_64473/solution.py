"""
QUESTION:
Develop a function called `find_indices` that takes two lists, `first_list` and `second_list`, as input and returns the indices of all elements from `second_list` that are found in `first_list`. The function should return a list of lists, where each inner list contains the indices of an element from `second_list` in `first_list`. If an element from `second_list` appears multiple times in `first_list`, all indices should be included. If an element from `second_list` does not exist in `first_list`, an empty list should be included in the output for that element.
"""

def find_indices(first_list, second_list):
    """
    This function finds the indices of all elements from second_list that are found in first_list.
    
    Args:
        first_list (list): The list in which to search for elements.
        second_list (list): The list containing elements to search for.
    
    Returns:
        list: A list of lists, where each inner list contains the indices of an element from second_list in first_list.
    """
    indices = []
    for num in second_list:
        index = [i for i, x in enumerate(first_list) if x==num]
        indices.append(index)
    return indices