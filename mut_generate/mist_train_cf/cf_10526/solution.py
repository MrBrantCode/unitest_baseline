"""
QUESTION:
Create a function `combine_lists_to_dict` that takes two lists, `list1` and `list2`, and returns a dictionary. The dictionary should include elements from `list1` as keys and corresponding elements from `list2` as values, stopping when `list2` is exhausted. The function should not include elements from `list1` that do not have corresponding elements in `list2`.
"""

def combine_lists_to_dict(list1, list2):
    """
    Creates a dictionary with elements from list1 as keys and corresponding elements from list2 as values.
    
    Args:
    list1 (list): The list of keys.
    list2 (list): The list of values.
    
    Returns:
    dict: A dictionary with elements from list1 as keys and corresponding elements from list2 as values.
    """
    return {list1[i]: list2[i] for i in range(min(len(list1), len(list2)))}