"""
QUESTION:
Create a function called `remove_duplicates` that takes a list containing integers and strings as input and returns a new list with duplicate elements removed while preserving the original order. The function should have a time complexity of O(n), where n is the length of the input list.
"""

def remove_duplicates(arr):
    seen = {}
    result = []
    
    for element in arr:
        if element not in seen:
            seen[element] = True
            result.append(element)
    
    return result