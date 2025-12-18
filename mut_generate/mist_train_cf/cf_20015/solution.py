"""
QUESTION:
Write a function binary_search_second_occurrence that takes a sorted list, a low index, a high index, a target element, and an optional first_occurrence index as parameters, and returns the index of the second occurrence of the target element in the list. If the target element does not have a second occurrence, the function should return -1. Assume the input list is sorted in ascending order and may contain duplicate elements.
"""

def binary_search_second_occurrence(arr, low, high, target, first_occurrence=None):
    if low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            if first_occurrence is None:
                # Found the first occurrence, continue searching for the second occurrence
                return binary_search_second_occurrence(arr, low, mid - 1, target, mid)
            elif arr[mid] != arr[first_occurrence]:
                # Found the second occurrence
                return mid
            else:
                # Continue searching for the second occurrence in the right half
                return binary_search_second_occurrence(arr, mid + 1, high, target, first_occurrence)
        
        elif arr[mid] < target:
            # Search in the right half
            return binary_search_second_occurrence(arr, mid + 1, high, target, first_occurrence)
        
        else:
            # Search in the left half
            return binary_search_second_occurrence(arr, low, mid - 1, target, first_occurrence)
    
    # Element not found
    return -1