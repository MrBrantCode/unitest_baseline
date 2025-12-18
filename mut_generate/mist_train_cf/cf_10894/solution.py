"""
QUESTION:
Create a function named `merge_dictionaries` that merges two input dictionaries. If a key exists in both dictionaries, multiply the corresponding values together; otherwise, use the value from either dictionary. The resulting merged dictionary must be sorted in ascending order by key.
"""

def entance(dict1, dict2):
    merged_dict = {}
    
    # Merge the dictionaries
    for key in dict1.keys():
        if key in dict2.keys():
            merged_dict[key] = dict1[key] * dict2[key]
        else:
            merged_dict[key] = dict1[key]
    
    for key in dict2.keys():
        if key not in dict1.keys():
            merged_dict[key] = dict2[key]
    
    # Sort the merged dictionary by keys in ascending order
    merged_dict = dict(sorted(merged_dict.items(), key=lambda x: x[0]))
    
    return merged_dict