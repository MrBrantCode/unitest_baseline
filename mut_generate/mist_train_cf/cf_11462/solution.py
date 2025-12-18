"""
QUESTION:
Create a function named `create_nested_dict` that takes two parameters: a list of strings and a list of lists of integers. The function should return a nested dictionary where the keys are the strings from the list, and the values are dictionaries with keys as integers from the corresponding inner list and values as the corresponding index of the integer. The indices in the inner dictionaries should be zero-based.
"""

def create_nested_dict(keys, values):
    """
    Creates a nested dictionary from two lists.
    
    Args:
    keys (list): A list of strings.
    values (list of lists): A list of lists of integers.
    
    Returns:
    dict: A nested dictionary where the keys are the strings from the list,
          and the values are dictionaries with keys as integers from the corresponding inner list
          and values as the corresponding index of the integer.
    """
    
    nested_dict = {}
    for i in range(len(keys)):
        inner_dict = {}
        for j in range(len(values[i])):
            inner_dict[values[i][j]] = j
        nested_dict[keys[i]] = inner_dict
    
    return nested_dict