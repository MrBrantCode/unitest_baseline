"""
QUESTION:
Create a function called "filter_square_dict_values" that takes in a dictionary as input and returns a new dictionary. The function should include the following restrictions and requirements:

* The input dictionary's keys and values must be integers.
* The function should only square and include the values that are positive in the new dictionary.
* The new dictionary should maintain the same keys as the input dictionary.

The function should return a new dictionary with the positive values squared.
"""

def filter_square_dict_values(dictionary):
    new_dict = {}
    
    if len(dictionary) == 0:
        return new_dict
    
    for key, value in dictionary.items():
        if not isinstance(key, int) or not isinstance(value, int):
            continue
        
        if value < 0:
            continue
        
        squared_value = value ** 2
        new_dict[key] = squared_value
    
    return new_dict