"""
QUESTION:
Construct a function named `construct_hierarchical_dict` that takes two parameters: `keys` and `values`, both of which are lists. The function should return a hierarchically structured dictionary where each key in the `keys` list is a nested dictionary, and the last value in the `values` list is assigned to the innermost dictionary. Ensure the function validates that the input lists are of the same length and are indeed lists. If not, it should return an informative error message.
"""

def construct_hierarchical_dict(keys, values):
    if len(keys) != len(values):
        return 'Error: Key and value lists are of different lengths.'
    
    if not (isinstance(keys, list) and isinstance(values, list)):
        return 'Error: Both inputs should be lists.'
    
    hierarchy_dict = {}
    current_dict = hierarchy_dict
    for i in range(len(keys)):
        current_dict[keys[i]] = {}
        current_dict = current_dict[keys[i]]
    current_dict.update(values[-1] if isinstance(values[-1], dict) else {values[-1]: None})

    return hierarchy_dict