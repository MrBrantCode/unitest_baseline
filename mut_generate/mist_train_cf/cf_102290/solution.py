"""
QUESTION:
Implement a function "remove_duplicates" that takes a list of objects as input and returns a list with removed duplicates, maintaining the original order. The input list can contain up to 10^6 objects of any type. The implementation should have a time complexity of O(n), where n is the number of objects in the input list, and use constant space (not using additional memory besides the input and output lists).
"""

def remove_duplicates(objects):
    seen = set()
    result = []
    
    for obj in objects:
        if obj not in seen:
            seen.add(obj)
            result.append(obj)
    
    return result