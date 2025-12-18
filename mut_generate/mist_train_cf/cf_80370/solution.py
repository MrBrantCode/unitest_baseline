"""
QUESTION:
Create two functions: `create_dict` and `compare_dict`. The `create_dict` function should take two lists of strings as arguments and return two dictionaries where the keys are the individual strings from the lists and the values denote the character count of those strings. The `compare_dict` function should take two dictionaries as inputs, compare the keys and values, and return a new dictionary with items that appear in both input dictionaries with the same keys and values. The `compare_dict` function must also handle erroneous input: if one or both of the provided dictionaries are empty, it should return an informative error message.
"""

def create_dict(arr1, arr2):
    dict1 = {i: len(i) for i in arr1}
    dict2 = {i: len(i) for i in arr2}
    
    return dict1, dict2

def compare_dict(dict1, dict2):
    if len(dict1) == 0 or len(dict2) == 0:
        return "Error: One or both of the input dictionaries are empty"
    
    shared_items = {k: dict1[k] for k in dict1 if k in dict2 and dict1[k] == dict2[k]}
    
    return shared_items