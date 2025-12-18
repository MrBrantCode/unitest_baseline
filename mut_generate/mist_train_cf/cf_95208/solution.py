"""
QUESTION:
Create a function called `create_nested_dict` that takes two lists, `l1` and `l2`, as input where `l1` contains strings and `l2` contains lists of integers. The function should return a nested dictionary where the keys are the strings from `l1` and the values are dictionaries with keys as integers from `l2` and values as the corresponding index of the integer in the second list. If there are duplicate values in the lists, the function should handle them by storing the indices in a list.
"""

def create_nested_dict(l1, l2):
    """
    Create a nested dictionary where the keys are the strings from l1 and the values are dictionaries 
    with keys as integers from l2 and values as the corresponding index of the integer in the second list.
    
    Args:
        l1 (list): A list of strings.
        l2 (list): A list of lists containing integers.
    
    Returns:
        dict: A nested dictionary.
    """
    nested_dict = {}
    
    for i in range(len(l1)):
        key = l1[i]
        values = l2[i]
        
        if key not in nested_dict:
            nested_dict[key] = {}
        
        for j in range(len(values)):
            value_key = values[j]
            
            if value_key not in nested_dict[key]:
                nested_dict[key][value_key] = []
            
            nested_dict[key][value_key].append(j)
    
    return nested_dict