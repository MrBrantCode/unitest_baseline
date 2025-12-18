"""
QUESTION:
Write a function `searchKeyDepth` that takes in a `searchKey` and a nested object `obj` to search for the key. The function should return the depth of the first occurrence of the `searchKey` if found, otherwise return -1. The depth is calculated from the root of the object (depth 1). You can assume that the values in the object are either integers or other objects.
"""

def searchKeyDepth(searchKey, obj, depth = 1):
    for key in obj:
        if key == searchKey:
            return depth
        elif isinstance(obj[key], dict):
            nestedDepth = searchKeyDepth(searchKey, obj[key], depth + 1);
            if nestedDepth != -1:
                return nestedDepth;
    return -1