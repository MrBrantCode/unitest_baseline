"""
QUESTION:
Implement the binary_search function that determines the index of an element in a given sorted array using the binary search algorithm. The function should take two parameters: a sorted array (arr) and the target element (element). It should return the index of the target element if found, and -1 if not found. The function should handle edge cases such as an empty array without using any pre-built functions.
"""

def entrance(arr, element):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < element:
            left = mid + 1
        elif arr[mid] > element:
            right = mid - 1
        else:
            return mid
    
    # When the element is not found, return -1
    return -1