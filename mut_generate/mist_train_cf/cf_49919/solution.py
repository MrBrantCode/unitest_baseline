"""
QUESTION:
Write a function `construct_nested_dict` that takes an array of tuples, where each tuple contains three string elements, and returns a tri-level nested dictionary. The outer key in the dictionary corresponds to the first element of the tuple, the inner key corresponds to the second element, and the inner-inner key corresponds to the third element. If a key does not exist in the dictionary, it should be created. The innermost key should have an empty dictionary as its value.
"""

def construct_nested_dict(keys):
    nested_dict = {}
    
    for key in keys:
        outer_key, inner_key, inner_inner_key = key
        
        if outer_key not in nested_dict:
            nested_dict[outer_key] = {}
        
        if inner_key not in nested_dict[outer_key]:
            nested_dict[outer_key][inner_key] = {}
            
        nested_dict[outer_key][inner_key][inner_inner_key] = {}
    
    return nested_dict