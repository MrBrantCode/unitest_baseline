"""
QUESTION:
Create a function named `create_nested_dict` that takes two parameters: a list of keys and a list of values. The function should return a nested dictionary where each key from the list of keys is mapped to the corresponding value from the list of values. If a key is a list, it should be treated as a nested key. The function should have a time complexity of O(n), where n is the length of the input list of keys. The function should not assume any specific length for the lists and should work for any valid input.
"""

def create_nested_dict(keys, values):
    """
    Creates a nested dictionary from a list of keys and a list of values.
    
    Args:
    keys (list): A list of keys. Nested keys are represented as lists.
    values (list): A list of values corresponding to the keys.
    
    Returns:
    dict: A nested dictionary where each key is mapped to its corresponding value.
    """
    nested_dict = {}
    for i in range(len(keys)):
        if isinstance(keys[i], list):
            nested_dict[keys[i][0]] = create_nested_dict(keys[i][1:], values[i:])
        else:
            nested_dict[keys[i]] = values[i]
    return nested_dict