"""
QUESTION:
Create a function `sort_dict` that takes a dictionary as input, sorts its keys in descending order, and sorts its values in ascending order. The function should return the sorted key-value pairs. Note that the relationship between the original keys and values may be lost due to independent sorting.
"""

def sort_dict(input_dict):
    """
    This function takes a dictionary as input, sorts its keys in descending order, 
    and sorts its values in ascending order. The function returns the sorted key-value pairs.
    
    Args:
        input_dict (dict): The input dictionary to be sorted.
    
    Returns:
        dict: A new dictionary with sorted keys in descending order and values in ascending order.
    """
    # Get dictionary keys, sort in descending order and store in a list
    keys = sorted(input_dict.keys(), reverse=True)
    
    # Get dictionary values, sort in ascending order and store in a list
    values = sorted(input_dict.values())
    
    # Create a new dictionary from the sorted keys and values
    new_dict = dict(zip(keys, values))
    
    return new_dict