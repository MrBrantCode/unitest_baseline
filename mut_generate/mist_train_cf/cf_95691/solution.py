"""
QUESTION:
Implement a function called "remove_duplicates" that takes a list of objects as input and returns a list with removed duplicates while maintaining the original order. The input list can contain up to 10^6 objects of any type. The function should have a time complexity of O(n), where n is the number of objects in the input list.
"""

def remove_duplicates(objects):
    seen = {}
    result = []
    
    for obj in objects:
        if obj not in seen:
            seen[obj] = True
            result.append(obj)
    
    return result