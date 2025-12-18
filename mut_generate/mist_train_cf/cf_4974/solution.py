"""
QUESTION:
Write a function `merge_dicts(dict1, dict2)` that merges two given dictionaries `dict1` and `dict2` into a single dictionary. The function should sum the values of duplicate keys and include only keys with values greater than or equal to 10 in the merged dictionary. The keys in the merged dictionary should be sorted in descending order based on their values.
"""

def merge_dicts(dict1, dict2):
    merged_dict = {}
    
    # Merge the dictionaries
    for key, value in dict1.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    
    # Sort the merged dictionary by values in descending order
    sorted_dict = {k: v for k, v in sorted(merged_dict.items(), key=lambda item: item[1], reverse=True)}
    
    # Filter out keys with values less than 10
    final_dict = {k: v for k, v in sorted_dict.items() if v >= 10}
    
    return final_dict