"""
QUESTION:
Write a function `remove_duplicates` that takes a list `arr` as input, removes duplicate elements while preserving the original order, and returns the resulting list. The list can contain both integers and strings. Do not use built-in functions or libraries for removing or checking duplicates. The function should have a time complexity of O(n), where n is the length of the list.
"""

def remove_duplicates(arr):
    seen = {}
    for element in arr:
        if element in seen:
            seen[element] = True
        else:
            seen[element] = False
    
    new_arr = []
    for element in arr:
        if not seen[element]:
            new_arr.append(element)
            seen[element] = True
    
    return new_arr