"""
QUESTION:
Write a function called `remove_duplicates` that takes a list containing integers and strings as input, removes duplicate elements while maintaining the original order, and returns the modified list.
"""

def remove_duplicates(arr):
    unique_set = set()
    modified_arr = []
    
    for elem in arr:
        if elem not in unique_set:
            unique_set.add(elem)
            modified_arr.append(elem)
    
    return modified_arr