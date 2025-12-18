"""
QUESTION:
Create a function named `swap_keys_values` that takes a dictionary `d` as input and returns a new dictionary with the keys and values swapped. If there are duplicate values in the original dictionary, the corresponding key in the new dictionary should hold a list of all original keys having that value.
"""

def swap_keys_values(d):
    """
    This function swaps keys and values of a dictionary.
    
    In case of duplicate values during the swap, the corresponding key will hold
    a list of all original keys having that value.
    """
    new_d = {}
    for k, v in d.items():
        if v in new_d:
            if type(new_d[v]) == list:
                new_d[v].append(k)
            else:
                new_d[v] = [new_d[v], k]
        else:
            new_d[v] = k
    return new_d