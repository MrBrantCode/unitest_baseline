"""
QUESTION:
Create a function `remove_duplicates` that takes an array as input, removes any duplicate elements while maintaining their original order, and returns the modified array. The array can contain both integers and strings. The function should have a time complexity of O(n), where n is the number of elements in the input array.
"""

def remove_duplicates(arr):
    unique_set = set()
    modified_arr = []
    
    for elem in arr:
        if elem not in unique_set:
            unique_set.add(elem)
            modified_arr.append(elem)
    
    return modified_arr