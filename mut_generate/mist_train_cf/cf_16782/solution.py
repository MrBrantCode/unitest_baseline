"""
QUESTION:
Write a function named `get_max_key` that takes a dictionary as input and returns the key corresponding to the maximum value in the dictionary. The function should not use the built-in `max()` function or any sorting functions. If the dictionary is empty, the function should return `None`.
"""

def get_max_key(dictionary):
    if len(dictionary) == 0:
        return None
    
    max_key = next(iter(dictionary))
    max_value = dictionary[max_key]
    
    for key, value in dictionary.items():
        if value > max_value:
            max_key = key
            max_value = value
    
    return max_key