"""
QUESTION:
Write a function `remove_duplicates(arr)` that takes an array of integers as input and returns the array with duplicate elements removed, while maintaining the original order of the remaining elements. The function must have a time complexity of O(n) and use a constant amount of additional space.
"""

def remove_duplicates(arr):
    unique_set = set()
    new_arr = []
    
    for element in arr:
        if element not in unique_set:
            unique_set.add(element)
            new_arr.append(element)
    
    return new_arr