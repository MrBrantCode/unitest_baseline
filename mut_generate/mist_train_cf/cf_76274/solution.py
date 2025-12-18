"""
QUESTION:
Write a function `modify_nested_dict` that takes in a dictionary, a list of keys representing the nested path to a specific value, and a new value. The function should modify the dictionary by updating the specified value without using built-in dictionary methods, and it should handle dictionaries with unspecified levels of depth. If the nested path does not exist in the dictionary, the function should raise an exception.
"""

def modify_nested_dict(dictionary, keys, new_value, depth=0):
    '''
    Modify a nested dictionary

    :param dictionary: The dictionary to modify
    :param keys: A list of keys leading to the value to modify
    :param new_value: The new value to set
    :param depth: The current depth in the dictionary
    :return: Nothing
    '''
    key = keys[depth]
    if depth + 1 == len(keys):
        dictionary[key] = new_value
        return
    else:
        if key in dictionary:
            modify_nested_dict(dictionary[key], keys, new_value, depth + 1)
        else:
            raise Exception("Key not found")