"""
QUESTION:
Implement the `binary_search` function to find the index of a given item in a sorted array. The function should take a sorted array and the target item as input and return the index of the item if found, or None if the item is not in the array. The array index starts from 0.
"""

def binary_search(array, item):
    low = 0
    high = len(array) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if array[mid] == item:
            return mid
        elif item < array[mid]:
            high = mid - 1
        else:
            low = mid + 1
    
    return None