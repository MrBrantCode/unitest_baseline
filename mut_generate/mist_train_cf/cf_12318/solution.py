"""
QUESTION:
Create a function called `merge_and_sort` that merges two input dictionaries into a single dictionary. The function should filter out keys with values less than 5, handle duplicate keys by summing their values, and sort the resulting dictionary in descending order by key values.
"""

def merge_and_sort(dict1, dict2):
    """
    Merges two input dictionaries into a single dictionary, filters out keys with values less than 5, 
    handles duplicate keys by summing their values, and sorts the resulting dictionary in descending order by key values.

    Args:
        dict1 (dict): The first dictionary to merge.
        dict2 (dict): The second dictionary to merge.

    Returns:
        dict: The merged and sorted dictionary.
    """

    merged_dict = {}
    
    # Iterate over the key-value pairs in the first dictionary
    for key, value in dict1.items():
        # Filter out keys with values less than 5
        if value >= 5:
            merged_dict[key] = value
    
    # Iterate over the key-value pairs in the second dictionary
    for key, value in dict2.items():
        # Filter out keys with values less than 5
        if value >= 5:
            # Handle duplicate keys by summing their values
            if key in merged_dict:
                merged_dict[key] += value
            else:
                merged_dict[key] = value
    
    # Sort the resulting dictionary in descending order by key values
    sorted_dict = dict(sorted(merged_dict.items(), key=lambda x: x[1], reverse=True))
    
    return sorted_dict