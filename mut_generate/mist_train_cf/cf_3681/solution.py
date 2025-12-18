"""
QUESTION:
Create a function `create_nested_dictionary(l1, l2)` where `l1` is a list of strings and `l2` is a list of lists of integers. The function should return a nested dictionary where the keys are the strings from `l1` and the values are dictionaries with keys as integers from `l2` and values as the corresponding index of the integer in `l2`. 

The function should handle cases where `l1` and `l2` have different lengths, where `l1` or `l2` contain non-string or non-integer values, and where `l2` contains nested lists. If `l1` contains duplicate values, the function should merge the corresponding dictionaries in the output.
"""

def create_nested_dictionary(l1, l2):
    nested_dict = {}
    
    min_length = min(len(l1), len(l2))
    
    for i in range(min_length):
        key = l1[i]
        value = l2[i]
        
        if not isinstance(key, str) or not isinstance(value, list):
            continue
        
        value = flatten_list(value)
        
        if key not in nested_dict:
            nested_dict[key] = {}
        
        for j, element in enumerate(value):
            if element in nested_dict[key]:
                nested_dict[key][element].append(i)
            else:
                nested_dict[key][element] = [i]
    
    return nested_dict


def flatten_list(lst):
    flattened_list = []
    
    for element in lst:
        if isinstance(element, list):
            flattened_list.extend(flatten_list(element))
        else:
            flattened_list.append(element)
    
    return flattened_list