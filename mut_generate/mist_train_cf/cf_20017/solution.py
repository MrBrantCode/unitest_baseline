"""
QUESTION:
Create a function named `create_dictionary` that takes two lists of integers as input. The function should return a dictionary where elements from the first list are keys and elements from the second list are values, with each key unique and only the last occurrence of a duplicate key included. The function should return an empty dictionary if the input lists are not of equal length or if a non-integer value is present in the second list. The function should have a time complexity not exceeding O(n^2), where n is the length of the input lists.
"""

def create_dictionary(keys, values):
    if len(keys) != len(values):
        return {}
    
    dictionary = {}
    
    for i in range(len(keys)):
        if isinstance(values[i], int):
            dictionary[keys[i]] = values[i]
    
    return dictionary