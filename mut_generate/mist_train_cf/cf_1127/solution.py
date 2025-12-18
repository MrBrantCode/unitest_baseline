"""
QUESTION:
Implement a function called `binary_search` that performs binary search on a given sorted list of numbers. The function should return the index of the target element if it is present in the list, or -1 if it is not present. The function should handle lists with duplicate elements by returning the index of any occurrence of the target element, and should also handle empty lists, non-sorted lists, and lists with non-numeric elements by returning -1 or an error message. The function should have a time complexity of O(log n), where n is the number of elements in the list.
"""

def binary_search(arr, target):
    # Check for empty list
    if len(arr) == 0:
        return -1
    
    # Check for non-numeric elements
    if not all(isinstance(x, (int, float)) for x in arr):
        return "Error: List contains non-numeric elements"
    
    # Check for non-sorted list
    if arr != sorted(arr):
        return "Error: List is not sorted"
    
    # Recursive binary search
    return binary_search_recursive(arr, target, 0, len(arr)-1)

def binary_search_recursive(arr, target, low, high):
    # Check for target out of range
    if target < arr[low] or target > arr[high]:
        return -1
    
    # Base case: target found
    if arr[low] == target:
        return low
    
    mid = (low + high) // 2

    # Check for target in the middle
    if arr[mid] == target:
        return mid
    
    # Recursive case: target in the left half
    if target < arr[mid]:
        return binary_search_recursive(arr, target, low, mid-1)
    
    # Recursive case: target in the right half
    return binary_search_recursive(arr, target, mid+1, high)