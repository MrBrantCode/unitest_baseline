"""
QUESTION:
Create a function named `create_dictionary` that takes two lists `keys` and `values` as input. The function should return a dictionary where elements from `keys` are the keys and elements from `values` are the values, with the last occurrence of each key included in case of duplicates. If the input lists are not of equal length, return an empty dictionary. Exclude any non-integer values from the `values` list. The function's time complexity should not exceed O(n^2), where n is the length of the input lists.
"""

def create_dictionary(keys, values):
    if len(keys) != len(values):
        return {}
    
    dictionary = {}
    
    for i in range(len(keys)):
        if isinstance(values[i], int):
            dictionary[keys[i]] = values[i]
    
    return dictionary