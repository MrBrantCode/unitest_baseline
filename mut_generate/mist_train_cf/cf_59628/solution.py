"""
QUESTION:
Create a function called `create_nested_dict` that generates a nested dictionary with alternating keys and values from two given lists of keys and values. The function should take two lists and an optional start index as parameters. The nested dictionary's depth should be equal to the number of elements in both lists, which should be the same. Implement this function using recursion.
"""

def create_nested_dict(list_keys, list_vals, start_index=0):
    """
    Generate a nested dictionary with alternating keys and values from two given lists of keys and values.

    Args:
        list_keys (list): A list of keys.
        list_vals (list): A list of values.
        start_index (int, optional): The index from where to start. Defaults to 0.

    Returns:
        dict: A nested dictionary with alternating keys and values.
    """
    if start_index == len(list_keys):
        return {}
    
    key = list_keys[start_index]
    val = list_vals[start_index]
    
    nest = create_nested_dict(list_keys, list_vals, start_index + 1)
    
    if nest:
        return {key: {val: nest}}
    else:
        return {key: val}