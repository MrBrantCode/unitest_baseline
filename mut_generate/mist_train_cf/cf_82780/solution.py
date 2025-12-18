"""
QUESTION:
Create a function `init_dict(keys, values)` to initialize a dictionary where `keys` is a list of dictionary keys and `values` is a list of corresponding values. The function should return a dictionary with the correct mapping of keys and values. Assume that the lengths of `keys` and `values` are equal.
"""

def init_dict(keys, values):
    """
    Initialize a dictionary with given keys and values.
    
    Args:
        keys (list): A list of dictionary keys.
        values (list): A list of corresponding values.
    
    Returns:
        dict: A dictionary with the correct mapping of keys and values.
    """
    return dict(zip(keys, values))