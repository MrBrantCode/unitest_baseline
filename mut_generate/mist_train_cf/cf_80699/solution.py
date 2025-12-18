"""
QUESTION:
Write a function `sort_dict_array` that takes in an array of dictionaries and a key as input, and returns the sorted array based on the given key. The function should handle the case where the specified key is not present in all dictionaries. If a dictionary is missing the key, it should be assigned a default value of infinity (`float('inf')`) for sorting purposes, placing it at the end of the sorted list.
"""

def sort_dict_array(array, key):
    return sorted(array, key = lambda k: k.get(key, float('inf')))