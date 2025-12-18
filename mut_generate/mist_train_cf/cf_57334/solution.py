"""
QUESTION:
Implement a function `ternary_search(list, key)` that performs a ternary search on a sorted list to find the index of a given key. The function should take two parameters: `list` (a sorted list of elements) and `key` (the element to search for). The function should return the index of the key if found, and -1 if the key is not in the list.
"""

def ternary_search(list, key):
    start = 0
    end = len(list) - 1
    while start <= end:
        mid1 = start + (end - start) // 3
        mid2 = end - (end - start) // 3
    
        if key == list[mid1]:
            return mid1
        if key == list[mid2]:
            return mid2
        if key < list[mid1]: 
            end = mid1 - 1 
        elif key > list[mid2]: 
            start = mid2 + 1
        else: 
            start = mid1 + 1
            end = mid2 - 1
    return -1  # Return -1 when key not in list