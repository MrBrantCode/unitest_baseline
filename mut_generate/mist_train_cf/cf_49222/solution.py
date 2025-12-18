"""
QUESTION:
Combine two dictionaries into one while maintaining the order of insertion. If there are key collisions, merge the values into a list. Implement a function `merge_dicts` that takes two dictionaries as input and returns the merged dictionary. The function should handle different data types and the resulting dictionary should preserve the insertion order.
"""

from collections import OrderedDict

def merge_dicts(dictA, dictB):
    """
    Merge two dictionaries into one while maintaining the order of insertion.
    If there are key collisions, merge the values into a list.
    
    Args:
    dictA (dict): The first dictionary to merge.
    dictB (dict): The second dictionary to merge.
    
    Returns:
    dict: The merged dictionary.
    """
    
    # Combine dictA and dictB into a new OrderedDict
    new_dict = OrderedDict()
    
    for d in (dictA, dictB):
        for key, value in d.items():
            if key in new_dict and new_dict[key] != value:
                # If the key exists and the value is not the same, append to list
                if not isinstance(new_dict[key], list):
                    new_dict[key] = [new_dict[key]]
                new_dict[key].append(value)
            else:
                new_dict[key] = value
                
    return new_dict