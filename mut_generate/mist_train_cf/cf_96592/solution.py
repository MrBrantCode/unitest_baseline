"""
QUESTION:
Find the index of the first occurrence of a given element in a sorted array with duplicate elements using binary search. The function should be able to handle arrays of up to 10^9 elements efficiently. Implement the `binary_search_with_duplicates(arr, target)` function, where `arr` is the sorted array and `target` is the target element. The function should return the index of the first occurrence of the target element if found, and -1 otherwise.
"""

def find_first_occurrence(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Look for duplicates on the left side
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result