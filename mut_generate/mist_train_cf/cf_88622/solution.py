"""
QUESTION:
Implement a function called "remove_duplicates" that takes a list of objects as input and returns a list with removed duplicates, maintaining the original order. The function should have a time complexity of O(n) and use constant space, excluding the input and output lists. The input list can contain up to 10^6 objects of any type.
"""

def remove_duplicates(objects):
    seen = set()
    result = []
    
    for obj in objects:
        if obj not in seen:
            seen.add(obj)
            result.append(obj)
    
    return result