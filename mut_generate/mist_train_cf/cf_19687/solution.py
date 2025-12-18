"""
QUESTION:
Write a function `merge_dicts(dict1, dict2)` that merges two dictionaries into a single dictionary. The merged dictionary should only include keys with values greater than or equal to 10. If there are duplicate keys, the value in the merged dictionary should be the product of the values from both dictionaries. The keys in the merged dictionary should be sorted in descending order based on their values.
"""

def merge_dicts(dict1, dict2):
    """
    Merges two dictionaries into a single dictionary.
    
    The merged dictionary only includes keys with values greater than or equal to 10.
    If there are duplicate keys, the value in the merged dictionary is the product of the values from both dictionaries.
    The keys in the merged dictionary are sorted in descending order based on their values.
    
    Parameters:
    dict1 (dict): The first dictionary.
    dict2 (dict): The second dictionary.
    
    Returns:
    dict: The merged dictionary.
    """
    merged_dict = {}
    
    # Merge dictionaries
    for key in dict1:
        if key in dict2:
            merged_dict[key] = dict1[key] * dict2[key]
        else:
            merged_dict[key] = dict1[key]
    
    for key in dict2:
        if key not in dict1:
            merged_dict[key] = dict2[key]
    
    # Sort keys in descending order based on values
    sorted_keys = sorted(merged_dict, key=lambda x: merged_dict[x], reverse=True)
    
    # Create new dictionary with sorted keys and values greater than or equal to 10
    new_dict = {}
    for key in sorted_keys:
        if merged_dict[key] >= 10:
            new_dict[key] = merged_dict[key]
    
    return new_dict