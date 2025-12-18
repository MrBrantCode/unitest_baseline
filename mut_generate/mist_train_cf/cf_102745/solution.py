"""
QUESTION:
Write a function `sort_list_of_dicts` that takes a list of dictionaries as input, filters out dictionaries that do not have the key 'age' or have non-integer 'age' values, and returns the filtered list sorted by 'age' values in ascending order.
"""

def sort_list_of_dicts(list_of_dicts):
    # Filter out dictionaries without the key 'age' and non-integer 'age' values
    valid_dicts = [d for d in list_of_dicts if 'age' in d and isinstance(d['age'], int)]
    
    # Sort the valid dictionaries by 'age' values in ascending order
    sorted_dicts = sorted(valid_dicts, key=lambda x: x['age'])
    
    return sorted_dicts