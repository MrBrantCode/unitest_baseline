"""
QUESTION:
Write a function `binary_search_second_occurrence(arr, low, high, target, first_occurrence)` that uses a recursive binary search algorithm to find the index of the second occurrence of the `target` element in a sorted list `arr` within the range `[low, high]`. The function should take into account the `first_occurrence` index to avoid searching for the first occurrence again. If the `target` element does not have a second occurrence, the function should return -1.
"""

def binary_search_second_occurrence(arr, low, high, target, first_occurrence):
    if low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            if first_occurrence is None:
                return binary_search_second_occurrence(arr, low, mid - 1, target, mid)
            elif arr[mid] != arr[first_occurrence]:
                return mid
            else:
                return binary_search_second_occurrence(arr, mid + 1, high, target, first_occurrence)
        
        elif arr[mid] < target:
            return binary_search_second_occurrence(arr, mid + 1, high, target, first_occurrence)
        
        else:
            return binary_search_second_occurrence(arr, low, mid - 1, target, first_occurrence)
    
    return -1