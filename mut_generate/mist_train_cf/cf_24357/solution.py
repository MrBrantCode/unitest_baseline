"""
QUESTION:
Write a function `remove_duplicates(arr)` that takes a list of integers as input and returns the list with all duplicates removed. The function should preserve the original order of elements in the list.
"""

def remove_duplicates(arr):
    result = [] 
    seen = set() 
    for item in arr:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result