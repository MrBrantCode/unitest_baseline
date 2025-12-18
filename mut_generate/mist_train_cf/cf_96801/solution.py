"""
QUESTION:
Create a dictionary with five keys where each key is assigned a sorted list of five values. Implement three functions: 
- `lookup_value(dictionary, key, index)` that efficiently looks up the value at a specified index in the list of a given key.
- `retrieve_indices(dictionary, key, value)` that efficiently retrieves the indices of a specified value in the list of a given key.
- `retrieve_values_in_range(dictionary, key, start_index, end_index)` that efficiently retrieves the values within a given range of indices from the list of a specified key.
"""

def lookup_value(dictionary, key, index):
    if key in dictionary:
        values_list = dictionary[key]
        if 0 <= index < len(values_list):
            return values_list[index]
    return None

def retrieve_indices(dictionary, key, value):
    if key in dictionary:
        values_list = dictionary[key]
        if value in values_list:
            return [i for i, v in enumerate(values_list) if v == value]
    return []

def retrieve_values_in_range(dictionary, key, start_index, end_index):
    if key in dictionary:
        values_list = dictionary[key]
        if 0 <= start_index <= end_index < len(values_list):
            return values_list[start_index:end_index+1]
    return []