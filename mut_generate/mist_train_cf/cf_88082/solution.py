"""
QUESTION:
Create a function named `create_nested_dictionary` that takes two lists `l1` and `l2` as input. The function should return a nested dictionary where the keys are the strings from `l1` and the values are dictionaries with keys as integers from `l2` and values as lists of indices where the integers appear in `l2` or its sublists. The function should handle cases where `l1` and `l2` have different lengths, contain non-integer values, or contain nested lists.
"""

def create_nested_dictionary(l1, l2):
    nested_dict = {}
    
    # Handling cases where the lists have different lengths
    min_length = min(len(l1), len(l2))
    
    def flatten_list(lst):
        flattened_list = []
        
        for element in lst:
            if isinstance(element, list):
                flattened_list.extend(flatten_list(element))
            else:
                flattened_list.append(element)
        
        return flattened_list
    
    for i in range(min_length):
        key = l1[i]
        value = l2[i]
        
        # Handling cases where the lists contain non-integer values
        if not isinstance(key, str) or not isinstance(value, list):
            continue
        
        # Handling cases where the lists contain nested lists
        value = flatten_list(value)
        
        if key not in nested_dict:
            nested_dict[key] = {}
        
        for j, element in enumerate(value):
            # Handling cases where the lists have duplicate values
            if element in nested_dict[key]:
                nested_dict[key][element].append(i)
            else:
                nested_dict[key][element] = [i]
    
    return nested_dict