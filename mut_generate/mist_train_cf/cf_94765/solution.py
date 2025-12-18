"""
QUESTION:
Create a function `remove_duplicates` that takes a list of mixed data types as input, removes duplicate elements while preserving the original order, and returns the new list. The function should achieve this with a time complexity of O(n), where n is the length of the input list.
"""

def remove_duplicates(arr):
    seen = {}
    result = []
    
    for element in arr:
        if element not in seen:
            seen[element] = True
            result.append(element)
    
    return result