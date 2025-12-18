"""
QUESTION:
Implement a function `merge_and_compare(dict1, dict2)` that merges two dictionaries and compares the differences between them. The function should return a new dictionary containing the union of keys from both input dictionaries. 

For keys present in both dictionaries, the resulting dictionary should contain the absolute difference between the two values. For keys found in only one of the input dictionaries, the resulting dictionary should contain the original key-value pair. 

Restrictions: The input dictionaries should only contain numeric values.
"""

def merge_and_compare(dict1, dict2):
    result = {}
    for key in set(dict1.keys()).union(dict2.keys()):
        if key in dict1 and key in dict2:
            result[key] = abs(dict1[key] - dict2[key])
        elif key in dict1: 
            result[key] = dict1[key]
        else:
            result[key] = dict2[key]
    return result