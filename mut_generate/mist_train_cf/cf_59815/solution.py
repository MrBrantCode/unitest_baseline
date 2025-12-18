"""
QUESTION:
Write a function `swap_dict_key_value(d)` that swaps key-value pairs in a dictionary `d`. If the original dictionary has multiple keys with the same value, the function should store these keys in a list as the value for the corresponding key in the swapped dictionary. The function should handle this case without raising any errors.
"""

def swap_dict_key_value(d):
    """ Swap keys and values in a dictionary """
    
    swapped_dict = {}
    for key, value in d.items():
        if value not in swapped_dict:
            # If value does not already exist as a key in the dictionary, add it
            swapped_dict[value] = key
        else:
            # If value exists as a key, append the new key to the list of keys for this value
            if not isinstance(swapped_dict[value], list):
                # If the value is not already in a list format, make it a list
                swapped_dict[value] = [swapped_dict[value]]
            swapped_dict[value].append(key)
    return swapped_dict