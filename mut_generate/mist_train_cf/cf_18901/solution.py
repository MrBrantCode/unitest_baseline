"""
QUESTION:
Create a function named `intersection_dicts` that takes two dictionaries `d1` and `d2` as input and returns a new dictionary containing the intersection of `d1` and `d2`. The intersection should include only keys that are present in both dictionaries and have the same values in both dictionaries. The function should handle cases where the values are lists or nested dictionaries, and should consider the elements in the lists and the nested dictionaries when checking for equality. If no intersection is found, the function should return an empty dictionary.
"""

def intersection_dicts(d1, d2):
    intersection = {}
    for key in d1.keys() & d2.keys():
        if isinstance(d1[key], dict) and isinstance(d2[key], dict):
            if d1[key] == d2[key]:
                intersection[key] = d1[key]
        elif isinstance(d1[key], list) and isinstance(d2[key], list):
            if d1[key] == d2[key]:
                intersection[key] = d1[key]
        else:
            if d1[key] == d2[key]:
                intersection[key] = d1[key]
    return intersection