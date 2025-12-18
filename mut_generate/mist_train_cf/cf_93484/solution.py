"""
QUESTION:
Implement a function `replace_value(dictionary, key, value)` that replaces the value at a given key in the dictionary and sorts the key-value pairs in ascending order based on the keys. The function should have a time complexity of O(log n) for the search and replacement operation, where n is the number of key-value pairs in the dictionary. The function should return a new dictionary with the sorted key-value pairs.
"""

import bisect

def replace_value(dictionary, key, value):
    # Get the keys and values as separate lists
    keys = list(dictionary.keys())
    values = list(dictionary.values())

    # Find the index of the key in the sorted list of keys using binary search
    index = bisect.bisect_left(keys, key)

    # If the key exists, replace the value at that index
    if index < len(keys) and keys[index] == key:
        values[index] = value
    # Otherwise, insert the key-value pair at the correct position
    else:
        keys.insert(index, key)
        values.insert(index, value)

    # Create a new dictionary with the sorted key-value pairs
    sorted_dict = {}
    for i in range(len(keys)):
        sorted_dict[keys[i]] = values[i]

    return sorted_dict