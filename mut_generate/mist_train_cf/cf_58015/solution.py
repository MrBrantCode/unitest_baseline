"""
QUESTION:
Create a Python function named `create_dict` that takes two lists as input, `keys` and `values`. The function should return a dictionary where the elements of `keys` are the keys and the elements of `values` are the corresponding values. The function must ensure that both lists have the same length and contain unique elements. If the length or uniqueness condition is not met, the function should return an error message.
"""

def create_dict(keys, values):
    if len(keys) != len(values) or len(keys) != len(set(keys)) or len(values) != len(set(values)):
        return "Both lists should be of equal length and contain unique elements."
    
    dictionary = {}
    for i in range(len(keys)):
        dictionary[keys[i]] = values[i]
    
    return dictionary