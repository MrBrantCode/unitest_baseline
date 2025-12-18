"""
QUESTION:
Create a function named `find_intersection` that takes two dictionaries `d1` and `d2` as input. The function should return a new dictionary containing the intersection between `d1` and `d2`, including keys that are present in both dictionaries and have the same values in both dictionaries. The comparison should consider values of type list and nested dictionaries as well. If no intersection is found, an empty dictionary should be returned.
"""

def find_intersection(d1, d2):
    intersection = {}
    
    for key in d1:
        if key in d2 and d1[key] == d2[key]:
            intersection[key] = d1[key]
        elif isinstance(d1[key], dict) and isinstance(d2[key], dict):
            nested_intersection = find_intersection(d1[key], d2[key])
            if nested_intersection:
                intersection[key] = nested_intersection
            
    return intersection