"""
QUESTION:
Create a function called `invert_and_sort_dict` that takes a dictionary as input and returns a new dictionary where the keys and values are swapped, the new keys are in descending order of their original order, and the new values are in ascending order of their original values.
"""

def invert_and_sort_dict(my_dict):
    inverted_dict = {}
    sorted_keys = sorted(my_dict.keys(), reverse=True)
    sorted_values = sorted(my_dict.values())
    
    for key, value in zip(sorted_keys, sorted_values):
        inverted_dict[value] = key
        
    return inverted_dict