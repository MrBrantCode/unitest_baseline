"""
QUESTION:
Create a function `is_subset` that takes two dictionaries, `main_dict` and `subset_dict`, as input. The function should return `True` if all keys in `subset_dict` are present in `main_dict`, and `False` otherwise. Assume that dictionary keys are unique.
"""

def is_subset(main_dict, subset_dict):
    """
    This function checks if all keys in subset_dict are present in main_dict.
    
    Args:
        main_dict (dict): The main dictionary.
        subset_dict (dict): The dictionary to be checked.
    
    Returns:
        bool: True if all keys in subset_dict are present in main_dict, False otherwise.
    """
    return set(subset_dict.keys()).issubset(set(main_dict.keys()))