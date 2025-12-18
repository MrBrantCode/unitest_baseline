"""
QUESTION:
Create a function `combine_lists` that takes two lists, `list_a` and `list_b`, as input and returns a new list. The function should add items from `list_a` that are greater than or equal to 3 and items from `list_b` that are less than or equal to 6, remove any duplicates, and sort the new list in ascending order.
"""

def combine_lists(list_a, list_b):
    """
    This function combines two lists, including items from list_a that are greater than or equal to 3 and 
    items from list_b that are less than or equal to 6, removes duplicates, and sorts the new list in ascending order.

    Args:
    list_a (list): The first input list.
    list_b (list): The second input list.

    Returns:
    list: A new list containing combined and filtered items from list_a and list_b.
    """
    # Filter items greater than or equal to 3 from list_a and less than or equal to 6 from list_b
    combined_list = [item for item in list_a if item >= 3] + [item for item in list_b if item <= 6]
    
    # Remove duplicates from the combined list and sort in ascending order
    return sorted(set(combined_list))